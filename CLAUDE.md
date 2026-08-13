> **CLAUDE: SUA PRIMEIRA AÇÃO É OBRIGATÓRIA.**
> Ao carregar este arquivo, execute a checagem de pasta abaixo, envie IMEDIATAMENTE a
> mensagem de boas-vindas e comece o setup. NÃO espere o usuário dizer nada. NÃO pergunte
> se pode começar. COMECE AGORA.

# Porta de entrada — Claude Code

> ⚠️ **Este arquivo é só a porta de entrada.** O roteiro completo do setup (Etapas 1 a 7,
> regras de comportamento e tabela de problemas comuns) está em **[`SETUP.md`](SETUP.md)**.
> Leia `SETUP.md` inteiro agora e siga à risca. Correções de setup se fazem lá, nunca aqui.

## Passo A — Confirme que está na pasta certa (antes de qualquer coisa)

**Execute:** `ls setup/check_prerequisites.py`

- **Encontrou** → vá para o Passo B.
- **Não encontrou** → **PARE.** Você está fora da pasta do produto. Não crie arquivos, não
  instale nada e **nunca construa um agente de WhatsApp do zero**. Mostre esta mensagem:

  > "Opa — parece que não estamos na pasta certa. Antes de continuar, digite `/exit` e
  > aperte Enter pra fechar. Depois cole isto no terminal:
  >
  > ```
  > git clone https://github.com/zxmarketingdigital/agente-ia-vendas.git
  > cd agente-ia-vendas
  > claude
  > ```
  >
  > Aí eu continuo daqui. 👍"

## Passo B — Mensagem de boas-vindas (copie exatamente)

> "Oi! 👋 Sou o Claude e vou configurar seu agente de vendas no WhatsApp agora mesmo — sem você precisar digitar nenhum comando.
>
> Deixa eu verificar primeiro se seu computador tem tudo instalado..."

## Passo C — Execute o setup

Leia **[`SETUP.md`](SETUP.md)** e execute da Etapa 1 até a Etapa 7, seguindo todas as
regras de comportamento descritas lá. Comece rodando `python3 setup/check_prerequisites.py`
(no Windows: `python setup\check_prerequisites.py`).
