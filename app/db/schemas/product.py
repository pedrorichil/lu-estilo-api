from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str = None
    price: float
    stock: int = 0

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str = None
    description: str = None
    price: float = None
    stock: int = None

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
