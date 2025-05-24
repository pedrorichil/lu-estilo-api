from sqlalchemy.orm import Session
from app.db.models.product import Product

def get_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

def get(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create(db: Session, product_data):
    product = Product(**product_data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update(db: Session, product: Product, update_data):
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete(db: Session, product: Product):
    db.delete(product)
    db.commit()
