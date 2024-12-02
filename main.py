from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import CRUD, Models
from app.DatabaseEngine import SessionLocal
from pydantic import BaseModel

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for user creation
class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = await CRUD.create_user(db=db, name=user.name, email=user.email)
    return db_user
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
