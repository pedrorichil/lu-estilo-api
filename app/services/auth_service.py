from datetime import timedelta
from app.core.security import create_access_token, verify_password
from app.db.crud import user as crud_user

def authenticate_user(db, username: str, password: str):
    user = crud_user.get_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_tokens(user):
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
