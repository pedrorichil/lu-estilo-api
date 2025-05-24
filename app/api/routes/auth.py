from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.schemas.user import UserCreate, UserLogin
from app.services import auth_service
from app.db.crud import user as crud_user
from app.core.security import create_access_token, decode_access_token


router = APIRouter()

@router.post("/auth/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = crud_user.create(db, user)
    return {"msg": "User created successfully"}

@router.post("/auth/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = auth_service.authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return auth_service.create_tokens(db_user)

@router.post("/auth/refresh-token")
def refresh_token(token: str):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    username = payload.get("sub")
    new_token = create_access_token({"sub": username})
    return {"access_token": new_token, "token_type": "bearer"}
