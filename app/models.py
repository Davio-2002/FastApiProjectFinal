from sqlalchemy import Column, Integer, String
from .database_config import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)