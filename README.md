# Agente IA de Vendas 🤖

Um **agente de vendas IA que responde no WhatsApp** sem código complicado. Setup em 15 minutos.

## ⚡ Quick Start

Cole no terminal o comando da IA que você escolheu — ela faz o resto:

```bash
# Gemini (grátis)
git clone https://github.com/zxmarketingdigital/agente-ia-vendas.git 2>/dev/null; cd agente-ia-vendas && gemini
```

```bash
# Codex
git clone https://github.com/zxmarketingdigital/agente-ia-vendas.git 2>/dev/null; cd agente-ia-vendas && codex
```

```bash
# Claude Code
git clone https://github.com/zxmarketingdigital/agente-ia-vendas.git 2>/dev/null; cd agente-ia-vendas && claude
```

> Já rodou esse comando antes e a pasta `agente-ia-vendas` já existe no seu computador? Sem problema — pode colar de novo, ele pula o clone e só continua de onde parou.

A IA abre automaticamente **dentro da pasta clonada** e conduz o setup por você. Se ela não
começar sozinha, digite `INICIAR SETUP`.

> 🛑 **O `cd agente-ia-vendas` não é opcional.** Se você abrir a IA fora dessa pasta, ela
> não encontra o roteiro do produto e começa a inventar um bot do zero (perguntando qual
> biblioteca usar, rodando `npm init`, etc.). Se isso acontecer, feche com `/exit` e cole o
> comando acima de novo.

## 📋 O que você vai ter

- ✅ Agente respondendo em tempo real no WhatsApp
- ✅ IA treinada com seu conteúdo (BANT methodology)
- ✅ Histórico de conversas salvo localmente
- ✅ Lead recebe checkout quando está pronto
- ✅ Sem servidor complicado — tudo local + Evolution API

## 🏗️ Arquitetura

### Stack
- **Evolution API** — Conexão com WhatsApp (open-source, gratuito)
- **SQLite** — Banco de dados local (sessões + histórico)
- **Python 3.9+** — Lógica do agente
- **Multi-IA** — OpenAI, Gemini ou Anthropic

### Fluxo

```
Usuário envia trigger
    ↓
Watcher detecta via Evolution API (polling a cada 3s)
    ↓
IA responde (BANT consultivo)
    ↓
Resposta enviada via Evolution API
    ↓
Conversa salva em SQLite (30 min TTL)
    ↓
Se purchase intent → envia checkout link
```

## 📁 Estrutura

```
agente-ia-vendas/
├── SETUP.md                           ← ROTEIRO CANÔNICO do setup (corrija aqui)
├── CLAUDE.md                          ← porta de entrada do Claude Code  ─┐
├── GEMINI.md                          ← porta de entrada do Gemini CLI   ─┼→ apontam p/ SETUP.md
├── AGENTS.md                          ← porta de entrada do Codex CLI    ─┘
├── README.md                          ← Documentação técnica
│
├── setup/
│   ├── check_prerequisites.py         ← Verifica dependências
│   ├── install_evolution.py           ← Instala Evolution API
│   ├── connect_whatsapp.py            ← Conecta WhatsApp via QR Code
│   ├── test_api.py                    ← Testa chave de IA
│   └── test_agent.py                  ← Simula conversa
│
├── templates/
│   ├── whatsapp/
│   │   ├── agent_template.py          ← Agente WhatsApp ({{placeholders}})
│   │   ├── watcher_template.py        ← Watcher (polling messages.json)
│   │   └── launchagent_template.plist ← Auto-restart macOS
│   │
│   └── shared/
│       ├── agent_core_template.py     ← Lógica IA (reutilizável)
│       └── sessions_template.py       ← SQLite operations
│
└── docs/
    ├── prerequisitos.md               ← Requisitos por SO
    └── guia.html                      ← Guia visual do setup
```

## 🎯 Exemplo de Uso

Seu lead envia:
> "Olá! Tenho uma dúvida sobre o Plano IA 2026."

Agente responde (2-3 segundos depois):
> "Oi! 👋 Que legal! O Plano IA 2026 foi feito pra quem quer construir negócio de IA do zero. Qual é sua dúvida específica? Estou aqui pra ajudar."

Depois de conversa consultiva (BANT):
> "Ótimo! Passei todas as suas infos aqui. Deixa eu enviar nosso checkout pra você dar uma olhada:
> [LINK_DE_COMPRA]"

Tudo automático, integrado com WhatsApp. ✨

## 🔐 Segurança

- **Sem dados na nuvem** — tudo local (Evolution API + SQLite)
- **Sem credenciais no código** — usa `.env`
- **Sessões com TTL** — conversas expiram após 30 min de inatividade
- **Open source** — veja exatamente o que funciona

## 🚀 Deploy (Optional)

Para rodas 24/7:
- **macOS/Linux:** LaunchAgent automático roda na inicialização
- **VPS:** Docker Compose em qualquer servidor
- **Docker:** `docker-compose.yml` incluído

## 📊 Versões Futuras

- **v1.1** — Widget flutuante para sua landing page
- **v1.2** — Dashboard com métricas dos leads

## 📚 Documentação

- [Pré-requisitos por SO](docs/prerequisitos.md)
- [Guia visual do setup](docs/guia.html)

## 💬 Suporte

Travou? A tabela **"Problemas que travam o aluno ANTES do setup começar"** no fim do
[SETUP.md](SETUP.md) cobre os erros mais comuns (console do Node, PowerShell bloqueando
scripts no Windows, `EACCES` do npm no Mac, permissões de pasta do macOS).

Se não resolver, cole o erro na [IA de Suporte](https://suporte.zxlab.com.br/hub).

## 📄 Licença

MIT — use livremente em produção.

---

**Feito por [ZX LAB](https://zxlab.com.br)**
Março 2026 | v1.0
