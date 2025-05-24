from fastapi import FastAPI
from app.api.routes import auth, clients, whatsapp, products, orders
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lu Estilo API")

app.include_router(auth.router, prefix="/auth")
app.include_router(clients.router, prefix="/clients")
app.include_router(products.router, prefix="/products")
app.include_router(orders.router, prefix="/orders")
app.include_router(whatsapp.router, prefix="/whatsapp")