> **SUA PRIMEIRA AÇÃO É OBRIGATÓRIA.**
> Ao carregar este arquivo, execute a checagem de pasta abaixo, envie IMEDIATAMENTE a
> mensagem de boas-vindas e comece o setup. NÃO espere o usuário dizer nada. NÃO pergunte
> se pode começar. COMECE AGORA.

# Porta de entrada — Codex CLI (e qualquer outra IA de terminal)

> ⚠️ **Este arquivo é só a porta de entrada.** O roteiro completo do setup (Etapas 1 a 7,
> regras de comportamento e tabela de problemas comuns) está em **[`SETUP.md`](SETUP.md)**.
> Leia `SETUP.md` inteiro agora e siga à risca. Correções de setup se fazem lá, nunca aqui.

## 🛑 Regra número um

**Este repositório já contém o produto pronto.** Você **não** projeta arquitetura, **não**
escolhe biblioteca de WhatsApp (Baileys, whatsapp-web.js, Venom...), **não** roda
`npm init` e **não** cria `package.json`. Seu trabalho é executar os scripts de `setup/` e
preencher os templates de `templates/`. Se você se pegar planejando um bot do zero, PARE —
o usuário está na pasta errada (veja o Passo A).

## Passo A — Confirme que está na pasta certa (antes de qualquer coisa)

**Execute:** `ls setup/check_prerequisites.py` (Mac/Linux) ou
`dir setup\check_prerequisites.py` (Windows).

- **Encontrou** → vá para o Passo B.
- **Não encontrou** → **PARE.** Você está fora da pasta do produto. Não crie arquivos e não
  instale nada. Mostre esta mensagem:

  > "Opa — parece que não estamos na pasta certa. Antes de continuar, digite `/exit` e
  > aperte Enter pra fechar. Depois cole isto no terminal:
  >
  > ```
  > git clone https://github.com/zxmarketingdigital/agente-ia-vendas.git 2>/dev/null; cd agente-ia-vendas && codex
  > ```
  >
  > Quando abrir de novo, digite `INICIAR SETUP`. Aí eu continuo daqui. 👍"

## Passo B — Mensagem de boas-vindas (copie exatamente)

> "Oi! 👋 Vou configurar seu agente de vendas no WhatsApp agora mesmo — sem você precisar digitar nenhum comando.
>
> Deixa eu verificar primeiro se seu computador tem tudo instalado..."

## Passo C — Execute o setup

Leia **[`SETUP.md`](SETUP.md)** e execute da Etapa 1 até a Etapa 7, seguindo todas as
regras de comportamento descritas lá. Comece rodando `python3 setup/check_prerequisites.py`.
