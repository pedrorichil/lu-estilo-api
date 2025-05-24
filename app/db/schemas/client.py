from pydantic import BaseModel, EmailStr

class ClientBase(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    phone_number: str = None

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    name: str = None
    email: EmailStr = None
    phone_number: str = None

class ClientResponse(ClientBase):
    id: int

    class Config:
        orm_mode = True
