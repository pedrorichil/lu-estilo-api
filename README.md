
---

### README atualizado com badges e instruções de uso:


# Lu Estilo API RESTful

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-313/)
[![FastAPI](https://img.shields.io/badge/FastAPI-v0.100-green)](https://fastapi.tiangolo.com/)
[![Tests](https://img.shields.io/github/actions/workflow/status/yourusername/lu_estilo_api/pytest.yml?branch=main&label=tests&logo=pytest)](#)
[![Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen)](#)
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/)

Estrutura de software recomendada para o desenvolvimento da API RESTful da Lu Estilo, com integração ao WhatsApp e atendendo a todos os requisitos especificados.

---

## ✅ Estrutura de Pastas
````
lu_estilo_api/
├── app/
│ ├── api/
│ │ ├── dependencies.py
│ │ ├── routes/
│ │ │ ├── auth.py
│ │ │ ├── clients.py
│ │ │ ├── products.py
│ │ │ ├── orders.py
│ │ │ └── whatsapp.py
│ ├── core/
│ │ ├── config.py
│ │ ├── security.py
│ │ └── logger.py
│ ├── db/
│ │ ├── base.py
│ │ ├── models/
│ │ │ ├── user.py
│ │ │ ├── client.py
│ │ │ ├── product.py
│ │ │ └── order.py
│ │ ├── schemas/
│ │ │ ├── user.py
│ │ │ ├── client.py
│ │ │ ├── product.py
│ │ │ └── order.py
│ │ ├── crud/
│ │ │ ├── user.py
│ │ │ ├── client.py
│ │ │ ├── product.py
│ │ │ └── order.py
│ │ └── session.py
│ ├── services/
│ │ ├── auth_service.py
│ │ └── whatsapp_service.py
│ ├── main.py
├── alembic/
│ ├── versions/
│ └── env.py
├── tests/
│ ├── test_auth.py
│ ├── test_clients.py
│ ├── test_products.py
│ ├── test_orders.py
│ └── test_whatsapp.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
````

---

## ✅ Instruções de Uso

### Pré-requisitos

- Python 3.13+
- Docker e Docker Compose (opcional, mas recomendado)
- PostgreSQL (local ou via Docker)

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/lu_estilo_api.git
cd lu_estilo_api
````

### 2. Configure variáveis de ambiente

Crie um arquivo `.env` na raiz com as configurações, por exemplo:

```env
DATABASE_URL=postgresql://postgres:senha@localhost:5432/lu_estilo_db
SECRET_KEY=uma_chave_secreta_muito_forte
WHATSAPP_API_URL=https://graph.facebook.com/v22.0/APP_ID_HERE/messages
WHATSAPP_TOKEN=token_aqui
WHATSAPP_PHONE_NUMBER_ID=Numero_Aqui
```

### 3. Instale dependências

Recomendo usar um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 4. Configure o banco de dados

* Se for usar local:

```bash
psql -U postgres -c "CREATE DATABASE lu_estilo_db;"
alembic upgrade head
```

* Se for usar Docker:

```bash
docker-compose up -d
```

### 5. Rode a API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:
[http://localhost:8000](http://localhost:8000)

### 6. Acesse a documentação interativa

Swagger UI:
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ Comandos úteis de teste

Para rodar os testes:

```bash
pytest -v
```



