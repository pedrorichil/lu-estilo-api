from sqlalchemy import Column, Integer, String, UniqueConstraint
from app.db.base import Base

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=True)

    __table_args__ = (UniqueConstraint('email', 'cpf', name='_email_cpf_uc'),)
