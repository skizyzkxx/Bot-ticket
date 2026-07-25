# 🎫 Discord Ticket Bot

Um bot Discord poderoso e funcional para gerenciar tickets de suporte em seu servidor!

## ✨ Recursos

- 🎟️ **Criação de Tickets** - Crie tickets de suporte privados com um comando simples
- 👥 **Gerenciamento de Acesso** - Adicione ou remova usuários dos tickets facilmente
- 📊 **Controle de Permissões** - Permissões automáticas para manter tickets privados
- 🎨 **Embeds Bonitos** - Interface visual atraente com embeds coloridos
- 📝 **Sistema Automático** - Numeração automática de tickets

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Um bot Discord (criar em [Discord Developer Portal](https://discord.com/developers/applications))

### Passos

1. **Clone ou baixe o projeto**
   ```bash
   git clone https://github.com/seu-usuario/discord-ticket-bot.git
   cd discord-ticket-bot
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**
   ```bash
   cp .env.example .env
   ```
   
   Edite o arquivo `.env` com seus valores:
   ```env
   DISCORD_TOKEN=seu_token_aqui
   PREFIX=!
   GUILD_ID=seu_guild_id_aqui
   ```

5. **Inicie o bot**
   ```bash
   python main.py
   ```

## 📋 Comandos

| Comando | Descrição |
|---------|-----------|
| `!create` | Cria um novo ticket de suporte |
| `!close` | Fecha e deleta o ticket atual |
| `!add <@user>` | Adiciona um usuário ao ticket |
| `!remove <@user>` | Remove um usuário do ticket |
| `!help` | Mostra a lista de comandos |

## 🔧 Configuração

### Permissões do Bot

Certifique-se de que seu bot tem as seguintes permissões:

- ✅ Manage Channels
- ✅ Send Messages
- ✅ Embed Links
- ✅ Read Message History
- ✅ Manage Permissions

### Variáveis de Ambiente

```env
DISCORD_TOKEN          # Token do seu bot Discord
PREFIX                 # Prefixo dos comandos (padrão: !)
MONGODB_URI           # URI do MongoDB (opcional)
GUILD_ID              # ID do servidor
SUPPORT_ROLE_ID       # ID da role de suporte (opcional)
LOG_CHANNEL_ID        # ID do canal de logs
```

## 📁 Estrutura do Projeto

```
discord-ticket-bot/
├── main.py                  # Arquivo principal do bot
├── requirements.txt         # Dependências Python
├── .env.example            # Exemplo de variáveis de ambiente
├── .env                    # Variáveis de ambiente (não commitar)
├── .gitignore             # Arquivos ignorados pelo git
├── .github/
│   └── workflows/
│       └── python.yml     # CI/CD workflow
└── README.md              # Este arquivo
```

## 🌟 Como Usar

1. **Criar um Ticket**
   ```
   !create
   ```
   Um novo canal privado será criado para você!

2. **Adicionar Suporte**
   ```
   !add @usuario
   ```

3. **Remover Usuário**
   ```
   !remove @usuario
   ```

4. **Fechar Ticket**
   ```
   !close
   ```
   O ticket será deletado após 5 segundos.

## 🛠️ Como Executar

```bash
# Com o ambiente virtual ativado
python main.py
```

## 📦 Dependências

- **discord.py** - Biblioteca para interagir com Discord API
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **pymongo** - Driver para MongoDB (opcional)

## 🐛 Troubleshooting

### Bot não responde
- Verifique se o token está correto no `.env`
- Certifique-se de que o bot tem permissões adequadas
- Verifique os logs do console para erros

### Permissões negadas
- Mova o bot para uma role mais alta na hierarquia
- Conceda as permissões necessárias

### Tickets não são criados
- Verifique se o bot tem permissão de criar canais
- Verifique se o bot tem permissão de gerenciar permissões

## 📄 Licença

MIT License - Veja LICENSE para detalhes

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues e pull requests.

## 💬 Suporte

Se precisar de ajuda:
1. Verifique os logs do console
2. Abra uma issue no GitHub
3. Visite a [documentação do discord.js](https://discord.js.org)

---

**Feito com ❤️ para a comunidade Discord**
