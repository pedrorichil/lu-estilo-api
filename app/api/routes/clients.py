from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.schemas.client import ClientCreate, ClientResponse, ClientUpdate
from app.db.crud import client as crud_client
from app.db.session import get_db

router = APIRouter()

@router.get("/clients", response_model=list[ClientResponse])
def list_clients(skip: int = 0, limit: int = 10, name: str = None, email: str = None, db: Session = Depends(get_db)):
    return crud_client.get_all(db, skip, limit, name, email)

@router.post("/clients", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return crud_client.create(db, client)

@router.get("/clients/{id}", response_model=ClientResponse)
def get_client(id: int, db: Session = Depends(get_db)):
    client = crud_client.get(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/clients/{id}", response_model=ClientResponse)
def update_client(id: int, client_update: ClientUpdate, db: Session = Depends(get_db)):
    client = crud_client.get(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return crud_client.update(db, client, client_update)

@router.delete("/clients/{id}")
def delete_client(id: int, db: Session = Depends(get_db)):
    client = crud_client.get(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    crud_client.delete(db, client)
    return {"msg": "Client deleted"}
