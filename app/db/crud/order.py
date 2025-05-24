from sqlalchemy.orm import Session
from app.db.models.order import Order
from app.db.models.product import Product

def get_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Order).offset(skip).limit(limit).all()

def get(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def create(db: Session, order_data):
    product = db.query(Product).filter(Product.id == order_data.product_id).first()
    if not product:
        return None
    total_price = product.price * order_data.quantity
    order = Order(**order_data.dict(), total_price=total_price)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def delete(db: Session, order: Order):
    db.delete(order)
    db.commit()
