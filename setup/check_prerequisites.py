#!/usr/bin/env python3
"""
check_prerequisites.py — Verifica se todos os pre-requisitos estao instalados.

Rodado pela IA na Etapa 1 do SETUP.md. Alem de conferir os programas, ele confirma
que estamos DENTRO da pasta do produto e que o clone esta completo — o erro numero 1
dos alunos (13/Ago/26: 8 compradores travados em 7 dias) e' abrir a IA na pasta errada,
e ai ela nao encontra o roteiro e comeca a inventar um bot do zero.

Compativel com Python 3.6+ de proposito: se o aluno tiver um Python antigo, ele precisa
ver a mensagem "sua versao e' antiga", nao um SyntaxError.
"""
import os
import re
import subprocess
import sys

REPO_URL = "https://github.com/zxmarketingdigital/agente-ia-vendas.git"

# Arquivos que provam que este e' o repositorio do produto, e nao uma pasta qualquer.
ARQUIVOS_ESSENCIAIS = [
    "SETUP.md",
    os.path.join("setup", "install_evolution.py"),
    os.path.join("setup", "connect_whatsapp.py"),
    os.path.join("templates", "whatsapp", "agent_template.py"),
    os.path.join("templates", "shared", "agent_core_template.py"),
]

# nome exibido, comando, versao minima (None = nao valida versao)
CHECKS = [
    ("Python 3.9+", "python3", (3, 9)),
    ("Node.js 18+", "node", (18,)),
    ("Git", "git", None),
    ("Docker", "docker", None),
]

INSTRUCOES = {
    "python3": [
        "macOS:   brew install python3",
        "Linux:   sudo apt install python3 python3-pip python3-venv",
        "Windows: baixe em https://www.python.org/downloads/ (marque 'Add to PATH')",
    ],
    "node": [
        "macOS:   brew install node   (ou baixe em https://nodejs.org/en/download)",
        "Linux:   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash && nvm install 18",
        "Windows: winget install OpenJS.NodeJS.LTS",
    ],
    "git": [
        "macOS:   brew install git",
        "Linux:   sudo apt install git",
        "Windows: winget install Git.Git",
    ],
    "docker": [
        "macOS/Windows: https://www.docker.com/products/docker-desktop",
        "Linux:         sudo apt install docker.io docker-compose",
    ],
}


def raiz_do_repo():
    """Raiz do produto, derivada do proprio arquivo — nao do diretorio atual.

    Assim o script funciona mesmo se a IA o chamar por caminho absoluto de outro lugar.
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def checar_pasta():
    """Confirma que o clone esta completo. Retorna a lista de arquivos faltando."""
    raiz = raiz_do_repo()
    return [rel for rel in ARQUIVOS_ESSENCIAIS
            if not os.path.isfile(os.path.join(raiz, rel))]


def extrair_versao(texto):
    """Primeiro numero de versao do texto: 'v18.20.4' -> (18, 20, 4)."""
    achado = re.search(r"(\d+)\.(\d+)(?:\.(\d+))?", texto or "")
    if not achado:
        return None
    return tuple(int(p) for p in achado.groups() if p is not None)


def rodar(args, timeout=10):
    """Executa e devolve (ok, saida). Nunca levanta excecao."""
    try:
        proc = subprocess.Popen(
            args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        saida = proc.communicate(timeout=timeout)[0]
        texto = (saida or b"").decode("utf-8", "replace").strip()
        return proc.returncode == 0, texto
    except subprocess.TimeoutExpired:
        proc.kill()
        return False, "tempo esgotado"
    except (OSError, ValueError):
        return False, ""


def checar_programa(nome, cmd, versao_minima):
    """Retorna (status, detalhe) onde status e' 'ok', 'ausente' ou 'antigo'."""
    ok, saida = rodar([cmd, "--version"])
    if not ok:
        return "ausente", ""

    primeira_linha = saida.split("\n")[0] if saida else "instalado"
    if versao_minima is None:
        return "ok", primeira_linha

    encontrada = extrair_versao(primeira_linha)
    if encontrada is None:
        # Nao conseguimos ler a versao: melhor deixar passar do que travar o aluno
        # por causa de um formato de saida inesperado.
        return "ok", primeira_linha
    if encontrada[:len(versao_minima)] < versao_minima:
        alvo = ".".join(str(n) for n in versao_minima)
        return "antigo", "%s (precisa ser %s ou maior)" % (primeira_linha, alvo)
    return "ok", primeira_linha


def docker_esta_rodando():
    """Docker instalado != Docker aberto. Fechado, a Etapa 2 falha com erro confuso."""
    ok, _ = rodar(["docker", "info"], timeout=20)
    return ok


def main():
    print("=" * 60)
    print("Verificando Pre-requisitos")
    print("=" * 60)

    # --- Etapa 0: estamos na pasta do produto? ------------------------------
    faltando_arquivos = checar_pasta()
    if faltando_arquivos:
        print("\n[X] PASTA ERRADA OU CLONE INCOMPLETO")
        print("=" * 60)
        print("\nNao encontrei estes arquivos do produto:")
        for rel in faltando_arquivos:
            print("   - %s" % rel)
        print("\nIA: PARE o setup aqui. Nao crie arquivos, nao instale nada e")
        print("NUNCA construa um agente de WhatsApp do zero. Peca ao usuario para")
        print("fechar a IA (/exit) e colar este comando no terminal:\n")
        print("   git clone %s 2>/dev/null; cd agente-ia-vendas\n" % REPO_URL)
        print("Depois abrir a IA de novo DENTRO dessa pasta e digitar INICIAR SETUP.")
        sys.exit(2)

    print("\n[OK] Pasta do produto confirmada:")
    print("     %s" % raiz_do_repo())

    # --- Programas ----------------------------------------------------------
    ausentes = []
    antigos = []
    for nome, cmd, versao_minima in CHECKS:
        status, detalhe = checar_programa(nome, cmd, versao_minima)
        if status == "ok":
            print("\n%-14s [OK] %s" % (nome + ":", detalhe))
        elif status == "antigo":
            print("\n%-14s [!]  %s" % (nome + ":", detalhe))
            antigos.append((nome, cmd))
        else:
            print("\n%-14s [X]  nao instalado" % (nome + ":"))
            ausentes.append((nome, cmd))

    # --- Docker precisa estar ABERTO, nao so instalado ----------------------
    docker_parado = False
    if not any(cmd == "docker" for _, cmd in ausentes):
        if docker_esta_rodando():
            print("\n%-14s [OK] em execucao" % "Docker ativo:")
        else:
            docker_parado = True
            print("\n%-14s [X]  instalado, mas NAO esta em execucao" % "Docker ativo:")

    problemas = ausentes + antigos

    if problemas or docker_parado:
        print("\n" + "=" * 60)
        print("Faltam dependencias")
        print("=" * 60)

        for nome, cmd in problemas:
            print("\n%s:" % nome)
            for linha in INSTRUCOES.get(cmd, []):
                print("  " + linha)

        if docker_parado:
            print("\nDocker esta instalado, mas o servico nao respondeu.")
            print("  macOS/Windows: abra o app Docker Desktop e espere o icone")
            print("                 da baleia ficar estavel.")
            print("  Linux:         sudo systemctl start docker")

        print("\nDepois de resolver, rode de novo:")
        print("  python3 setup/check_prerequisites.py\n")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("[OK] Todos os pre-requisitos estao instalados!")
    print("=" * 60)
    print("\nProxima etapa:")
    print("  python3 setup/install_evolution.py\n")


if __name__ == "__main__":
    main()
