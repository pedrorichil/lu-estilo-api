from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.schemas.order import OrderCreate, OrderResponse
from app.db.crud import order as crud_order
from app.db.session import get_db

router = APIRouter()

@router.get("/orders", response_model=list[OrderResponse])
def list_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_order.get_all(db, skip, limit)

@router.post("/orders", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = crud_order.create(db, order)
    if not new_order:
        raise HTTPException(status_code=404, detail="Product not found")
    return new_order

@router.get("/orders/{id}", response_model=OrderResponse)
def get_order(id: int, db: Session = Depends(get_db)):
    order = crud_order.get(db, id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/orders/{id}")
def delete_order(id: int, db: Session = Depends(get_db)):
    order = crud_order.get(db, id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    crud_order.delete(db, order)
    return {"msg": "Order deleted"}

