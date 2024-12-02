from sqlalchemy.orm import Session
from app import Models

def get_user(db: Session, user_id: int):
    return db.query(Models.User).filter(Models.User.id == user_id).first()

async def create_user(db: Session, name: str, email: str):
    db_user = Models.User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
