
---

# 🚨 PolkaAlert

**PolkaAlert** é um projeto em Python para automação de notificações via Telegram, com funcionalidades de extração de dados, manipulação de banco de dados e monitoramento de preços. 🎯

---

## 📂 Estrutura do Projeto

A organização dos arquivos é a seguinte:

```
polkaalert/
│
├── bot_telegram.py       # 🤖 Código para integração com o Telegram
├── db_utils.py           # 🗄️ Utilitários para o banco de dados
├── extract_price.py      # 💹 Script para extração de preços
├── main.py               # 🚀 Script principal para executar o pipeline
│
└── tests/                # ✅ Pasta com os testes
```

---

## 🛠️ Pré-requisitos

Certifique-se de ter o [Poetry](https://python-poetry.org/) instalado para gerenciar dependências do projeto.

### 🧩 Dependências principais

- 🐍 **Python**: `^3.12`
- 📊 **Pandas**: `^2.2.3`
- 🌐 **Requests**: `^2.32.3`
- 🔑 **Python-dotenv**: `^1.0.1`
- 🛠️ **SQLAlchemy**: `^2.0.36`
- ✈️ **Python Telegram Bot**: `^21.7`

---

## ⚡ Instalação

Siga os passos abaixo para configurar o projeto:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/polkaalert.git
   cd polkaalert
   ```

2. **Instale as dependências** com o Poetry:

   ```bash
   poetry install
   ```

3. **Configure o arquivo `.env`** com as suas variáveis de ambiente:

   Exemplo:
   ```
   TELEGRAM_BOT_TOKEN=seu_token_aqui
   DATABASE_URL=sua_url_do_banco_aqui
   ```

---

## 🚀 Como Usar

1. Certifique-se de que o banco de dados está configurado e acessível. 🗄️
2. Execute o script principal: 

   ```bash
   poetry run python polkaalert/main.py
   ```

---