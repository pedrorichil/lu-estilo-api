from sqlalchemy.orm import Session
from app.db.models.user import User
from app.core.security import get_password_hash, verify_password

def get_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create(db: Session, user_data):
    hashed_pw = get_password_hash(user_data.password)
    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_pw
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
