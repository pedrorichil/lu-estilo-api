from pydantic import BaseModel

class OrderBase(BaseModel):
    client_id: int
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    total_price: float

    class Config:
        from_attributes = True
