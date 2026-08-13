# Pré-requisitos por Sistema Operacional

> **Você só instala duas coisas na mão: o Node.js e a CLI da IA.**
> Python, Git e Docker são conferidos pela própria IA na Etapa 1 do setup — se faltar
> algum, ela te dá o comando exato para o seu sistema antes de continuar. Não saia
> instalando tudo desta página por precaução.
>
> Passo a passo completo com prints: **https://zxlab.com.br/instalar-agente-ia**

---

## 1. Node.js (obrigatório — é o que faz a CLI da IA funcionar)

| Sistema | Como instalar |
|---|---|
| **macOS** | Baixe em [nodejs.org/en/download](https://nodejs.org/en/download) (mais fácil) ou `brew install node` |
| **Windows** | `winget install OpenJS.NodeJS.LTS` no PowerShell, ou baixe em [nodejs.org/en/download](https://nodejs.org/en/download) |
| **Linux** | `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh \| bash` e depois `nvm install 18` |

Confira depois de instalar:

```bash
node --version    # precisa ser 18 ou maior
```

> ⚠️ **Digite `node --version`, não `node` sozinho.** Digitar só `node` te joga no console
> interno do Node (o prompt vira `>`) e qualquer comando depois disso dá
> `Uncaught SyntaxError`. Se cair nele, digite `.exit` e tente de novo.

---

## 2. A CLI da IA (escolha UMA)

| IA | Comando | Custo |
|---|---|---|
| **Gemini** — recomendada | `npm install -g @google/gemini-cli` | Grátis |
| **Codex** | `npm install -g @openai/codex` | Grátis por tempo limitado |
| **Claude Code** | `npm install -g @anthropic-ai/claude-code` | Exige assinatura Claude Pro (~US$20/mês) |

> 🔴 **Claude Code precisa da assinatura Pro, não de créditos de API.** São coisas
> diferentes — você não precisa comprar crédito no console da Anthropic para instalar o
> agente. E ninguém é obrigado a pagar nada: o setup inteiro roda de graça no Gemini.

### Se der erro no `npm install -g`

| Erro | Sistema | Correção |
|---|---|---|
| `gemini.ps1 não pode ser carregado porque a execução de scripts foi desabilitada` | Windows | Abra o PowerShell **como Administrador**, rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, confirme com `S`, feche e reabra o terminal. Vale para `gemini`, `codex` e `claude`. |
| `npm error code EACCES ... permission denied, mkdir '/usr/local/lib/node_modules/...'` | macOS | `sudo chown -R $(whoami) /usr/local/lib/node_modules /usr/local/bin` e repita o `npm install -g` |

---

## 3. O que a IA confere sozinha na Etapa 1

Você **não precisa** instalar isto antes. A IA roda `setup/check_prerequisites.py`, detecta
o que falta e te passa o comando certo para o seu sistema.

### Python 3.9+

```bash
# macOS
brew install python3

# Linux
sudo apt update && sudo apt install python3 python3-pip python3-venv

# Windows — já vem com o instalador oficial em python.org/downloads
```

### Git

```bash
# macOS
brew install git

# Linux
sudo apt install git

# Windows
winget install Git.Git
```

### Docker (usado na Etapa 2, para subir a Evolution API)

- **macOS / Windows:** baixe o Docker Desktop em
  [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).
  No Windows o próprio instalador configura o WSL2 por baixo — você não precisa rodar
  `wsl --install` na mão.
- **Linux:** `sudo apt install docker.io docker-compose` e depois
  `sudo usermod -aG docker $USER` (é preciso sair e entrar na sessão para valer).

> ⚠️ **Não basta instalar — o Docker precisa estar ABERTO e rodando.** No macOS e no
> Windows, abra o app Docker Desktop e espere o ícone da baleia ficar estável antes de
> seguir. Instalado mas fechado faz a Etapa 2 falhar com um erro confuso.

---

## Verificar tudo de uma vez

Dentro da pasta `agente-ia-vendas`:

```bash
python3 setup/check_prerequisites.py
```

> Se aparecer `can't open file ... check_prerequisites.py`, você está fora da pasta do
> produto. Rode `cd agente-ia-vendas` primeiro — ou refaça o clone conforme o
> [README](../README.md).

---

## Observações de plataforma

- **macOS e Linux** rodam o agente nativamente.
- **Windows** funciona para o setup e para rodar o agente, mas o **auto-start automático
  (LaunchAgent) é exclusivo do macOS** — no Windows o watcher precisa ser iniciado
  manualmente ou agendado pelo Agendador de Tarefas.
