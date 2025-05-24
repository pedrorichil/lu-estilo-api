from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.db.crud import product as crud_product
from app.db.session import get_db

router = APIRouter()

@router.get("/products", response_model=list[ProductResponse])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_product.get_all(db, skip, limit)

@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create(db, product)

@router.get("/products/{id}", response_model=ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    product = crud_product.get(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{id}", response_model=ProductResponse)
def update_product(id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    product = crud_product.get(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud_product.update(db, product, product_update)

@router.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    product = crud_product.get(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    crud_product.delete(db, product)
    return {"msg": "Product deleted"}
