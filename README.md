**Estrutura de software** recomendada para o desenvolvimento da API RESTful da Lu Estilo, com integração ao WhatsApp e atendendo a todos os requisitos especificados.

---

## ✅ Estrutura de Pastas

```
lu_estilo_api/
├── app/
│   ├── api/
│   │   ├── dependencies.py
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── clients.py
│   │   │   ├── products.py
│   │   │   ├── orders.py
│   │   │   └── whatsapp.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logger.py
│   ├── db/
│   │   ├── base.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── client.py
│   │   │   ├── product.py
│   │   │   └── order.py
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   ├── client.py
│   │   │   ├── product.py
│   │   │   └── order.py
│   │   ├── crud/
│   │   │   ├── user.py
│   │   │   ├── client.py
│   │   │   ├── product.py
│   │   │   └── order.py
│   │   └── session.py
│   ├── services/
│   │   ├── whatsapp_service.py
│   │   └── auth_service.py
│   ├── main.py
├── alembic/
│   ├── versions/
│   └── env.py
├── tests/
│   ├── test_auth.py
│   ├── test_clients.py
│   ├── test_products.py
│   ├── test_orders.py
│   └── test_whatsapp.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ✅ Descrição dos Componentes

### **1. app/api/routes/**

* **auth.py** → Endpoints de autenticação (`/auth/login`, `/auth/register`, `/auth/refresh-token`).
* **clients.py** → CRUD de clientes.
* **products.py** → CRUD de produtos.
* **orders.py** → CRUD de pedidos.
* **whatsapp.py** → Endpoint para enviar mensagens via WhatsApp.

---

### **2. app/core/**

* **config.py** → Configurações gerais do app (chaves, variáveis de ambiente).
* **security.py** → Funções para geração/validação de JWT, hashing de senhas.
* **logger.py** → Configuração de logging e integração com Sentry.

---

### **3. app/db/**

* **models/** → ORM (SQLAlchemy) para User, Client, Product, Order.
* **schemas/** → Schemas Pydantic para validação e serialização.
* **crud/** → Funções CRUD para acesso ao banco.
* **session.py** → Gerenciamento da sessão com o banco de dados.
* **base.py** → Base declarativa do SQLAlchemy.

---

### **4. app/services/**

* **auth\_service.py** → Lógica de autenticação, geração de tokens.
* **whatsapp\_service.py** → Integração com API do WhatsApp (Ex: Twilio, Meta Cloud API).

---

### **5. app/main.py**

* Arquivo principal, instancia `FastAPI`, inclui routers, middlewares, e CORS.

---

## ✅ Banco de Dados

* PostgreSQL com migrações via Alembic.
* Índices:

  * **Email e CPF** únicos em `Client`.
  * **Código de barras** e **descrição** indexados em `Product`.
  * **id\_pedido**, **status** e **cliente\_id** indexados em `Order`.

---

## ✅ Autenticação e Autorização

* JWT via **PyJWT**.
* Níveis de acesso:

  * `admin`: pode gerenciar usuários, produtos e pedidos.
  * `user`: pode consultar produtos e criar pedidos.
* Middleware para proteger rotas.

---

## ✅ Integração com WhatsApp

* **Endpoint**: `POST /whatsapp/send`
* **Payload**: `{ "client_id": int, "message": str }`
* Serviço `whatsapp_service.py` faz chamada para a API oficial.

---

## ✅ Tratamento de Erros

* **HTTPException** com mensagens padrão.
* **Validações** com Pydantic.
* **Logging** de erros com **Sentry**.

---

## ✅ Testes

* `pytest`
* **Cobertura**:

  * Unitários: serviços, validações.
  * Integração: endpoints.
* Mock da API do WhatsApp.

---

## ✅ Documentação

* **Swagger** automático com FastAPI.
* **OpenAPI** gerado com exemplos e descrições detalhadas.

---

## ✅ Deploy

* **Docker** para facilitar ambiente.
* Arquivos:

  * `Dockerfile` → Imagem da API.
  * `docker-compose.yml` → Banco PostgreSQL + API.

---

## ✅ Requisitos no `requirements.txt`

```
fastapi
uvicorn
SQLAlchemy
psycopg2-binary
python-dotenv
passlib[bcrypt]
PyJWT
alembic
pydantic[email]
httpx
pytest
sentry-sdk
```

---

## ✅ Fluxo de Desenvolvimento

1. **Modelagem** do banco.
2. **CRUD** para `User`, `Client`, `Product`, `Order`.
3. **Autenticação** com JWT.
4. **Integração** com WhatsApp.
5. **Testes** com pytest.
6. **Documentação** no Swagger.
7. **Deploy** via Docker.

---

## ✅ Exemplo de Endpoint de Envio via WhatsApp

```python
@router.post("/whatsapp/send")
async def send_whatsapp_message(client_id: int, message: str, db: Session = Depends(get_db)):
    client = crud_client.get(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    success = whatsapp_service.send_message(client.phone_number, message)
    if not success:
        raise HTTPException(status_code=500, detail="Erro ao enviar mensagem")
    
    return {"status": "Mensagem enviada com sucesso"}
```
