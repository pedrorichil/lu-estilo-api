from fastapi import FastAPI
from app.api.routes import auth, clients, whatsapp, products, orders
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lu Estilo API")

app.include_router(auth.router)
app.include_router(clients.router)
app.include_router(whatsapp.router)
app.include_router(products.router)
app.include_router(orders.router)