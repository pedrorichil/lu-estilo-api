from sqlalchemy.orm import Session
from app.db.models.client import Client

def get_all(db: Session, skip: int = 0, limit: int = 10, name: str = None, email: str = None):
    query = db.query(Client)
    if name:
        query = query.filter(Client.name.ilike(f"%{name}%"))
    if email:
        query = query.filter(Client.email.ilike(f"%{email}%"))
    return query.offset(skip).limit(limit).all()

def get(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def create(db: Session, client_data):
    client = Client(**client_data.dict())
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

def update(db: Session, client: Client, update_data):
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(client, key, value)
    db.commit()
    db.refresh(client)
    return client

def delete(db: Session, client: Client):
    db.delete(client)
    db.commit()
