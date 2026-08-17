# Pré-requisitos por Sistema Operacional

> **Você instala na mão: o Python, o Node.js e a CLI da IA.**
> Git e Docker são conferidos pela própria IA na Etapa 1 do setup — se faltar algum,
> ela te dá o comando exato para o seu sistema antes de continuar. Não saia instalando
> tudo desta página por precaução.
>
> O Python entra nessa lista porque a verificação da Etapa 1 **é um script Python**:
> sem ele, a IA não consegue nem rodar o check. No macOS e no Linux ele já vem
> instalado — na prática, só quem está no Windows precisa instalar.
>
> Passo a passo completo com prints: **https://zxlab.com.br/instalar-agente-ia**

---

## 1. Node.js (obrigatório — é o que faz a CLI da IA funcionar)

| Sistema | Como instalar |
|---|---|
| **macOS** | Baixe em [nodejs.org/en/download](https://nodejs.org/en/download) (mais fácil) ou `brew install node` |
| **Windows** | `winget install OpenJS.NodeJS.LTS` no PowerShell, ou baixe em [nodejs.org/en/download](https://nodejs.org/en/download) |
| **Linux** | Ver o bloco abaixo — o nvm precisa ser carregado antes de usar |

No Linux, cole as três linhas juntas (a do meio é o que faz o `nvm` existir na sessão
atual — sem ela o `nvm install` responde `command not found`):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
export NVM_DIR="$HOME/.nvm" && . "$NVM_DIR/nvm.sh"
nvm install 20
```

Confira depois de instalar:

```bash
node --version    # precisa ser 20 ou maior
```

> ⚠️ **O piso do produto é Node 20** — é o que a Gemini (opção recomendada) exige, e o
> Codex também roda nele. **O Claude Code exige Node 22.** Na dúvida, instale a versão
> LTS mais recente: ela atende as três.

> ⚠️ **Digite `node --version`, não `node` sozinho.** Digitar só `node` te joga no console
> interno do Node (o prompt vira `>`) e qualquer comando depois disso dá
> `Uncaught SyntaxError`. Se cair nele, digite `.exit` e tente de novo.

---

## 2. A CLI da IA (escolha UMA)

| IA | Comando | Node mínimo | Custo |
|---|---|---|---|
| **Gemini** — recomendada | `npm install -g @google/gemini-cli` | 20+ | Grátis |
| **Codex** | `npm install -g @openai/codex` | 20+ | Grátis por tempo limitado |
| **Claude Code** | `npm install -g @anthropic-ai/claude-code` | 22+ | Exige assinatura Claude Pro (~US$20/mês) |

> 🔴 **Claude Code precisa da assinatura Pro, não de créditos de API.** São coisas
> diferentes — você não precisa comprar crédito no console da Anthropic para instalar o
> agente. E ninguém é obrigado a pagar nada: o setup inteiro roda de graça no Gemini.

### Se der erro no `npm install -g`

| Erro | Sistema | Correção |
|---|---|---|
| `gemini.ps1 não pode ser carregado porque a execução de scripts foi desabilitada` | Windows | Abra o PowerShell **normal** (NÃO precisa ser Administrador — `-Scope CurrentUser` altera só o seu perfil de usuário), rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, confirme com `S`, **feche e reabra** o terminal. Vale para `gemini`, `codex` e `claude`. |
| `npm error code EACCES ... permission denied, mkdir '/usr/local/lib/node_modules/...'` | macOS / Linux | Instale o Node por um gerenciador do próprio usuário (`brew install node` no macOS, nvm no Linux) e repita o `npm install -g` — assim não precisa de permissão especial. Se não der, aí sim repita o **mesmo comando da IA que você escolheu** com `sudo` na frente (ex.: `sudo npm install -g @google/gemini-cli`) |

> ⚠️ **Não use `sudo chown -R` em `/usr/local/bin`** para resolver o EACCES. É uma
> "solução" que circula na internet e ela reescreve o dono de programas que não têm
> nada a ver com o npm, o que quebra atualizações depois. Instalar o Node por `brew`/nvm
> (ou, em último caso, rodar o próprio `npm install -g` com `sudo`) resolve o mesmo
> problema sem mexer em nada mais.

---

## 3. Python 3.9+ (só instale se o comando abaixo falhar)

```bash
# macOS e Linux — teste primeiro, quase sempre já está instalado
python3 --version    # precisa ser 3.9 ou maior

# Windows (PowerShell) — teste primeiro
python --version     # precisa ser 3.9 ou maior
```

Se o comando não existir **ou a versão for menor que 3.9**:

```bash
# macOS
brew install python3

# Linux
sudo apt update && sudo apt install python3 python3-pip python3-venv

# Windows — baixe em https://www.python.org/downloads/ e MARQUE "Add python.exe to PATH"
```

> ⚠️ **No Windows o comando é `python`, não `python3`.** Se você digitar `python3`, o
> Windows abre a Microsoft Store em vez de rodar o Python — é um atalho do sistema, não
> um erro seu. Use `python` (ou `py`).

---

## 4. O que a IA confere sozinha na Etapa 1

Você **não precisa** instalar isto antes. A IA roda o script de verificação, detecta o
que falta e te passa o comando certo para o seu sistema.

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
- **Linux:** siga o guia oficial da sua distribuição em
  [docs.docker.com/engine/install](https://docs.docker.com/engine/install/) — ele já
  instala o Docker **e** o plugin `docker compose` juntos. Depois rode
  `sudo usermod -aG docker $USER` (é preciso sair e entrar na sessão para valer).
  O `sudo apt install docker.io docker-compose-plugin` só funciona se o repositório do
  Docker já estiver configurado — em Ubuntu/Debian padrão ele falha com
  `Unable to locate package docker-compose-plugin`.

> ⚠️ **No Linux tem que ser o `docker-compose-plugin`, não o `docker-compose` antigo.**
> A Etapa 2 roda `docker compose up` (com espaço, versão 2). Quem instala só o pacote
> `docker-compose` (com hífen, versão 1) passa na verificação e trava depois, na hora de
> subir a Evolution API. O Docker Desktop do macOS e do Windows já vem com o plugin.

> ⚠️ **Não basta instalar — o Docker precisa estar ABERTO e rodando.** No macOS e no
> Windows, abra o app Docker Desktop e espere o ícone da baleia ficar estável antes de
> seguir. Instalado mas fechado faz a Etapa 2 falhar com um erro confuso.

---

## Verificar tudo de uma vez

Dentro da pasta `agente-ia-vendas`:

```bash
# macOS / Linux
python3 setup/check_prerequisites.py
```

```powershell
# Windows (PowerShell)
python setup\check_prerequisites.py
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
