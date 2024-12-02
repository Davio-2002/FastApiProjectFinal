from app.DatabaseEngine import engine
from app.Models import Base

Base.metadata.create_all(bind=engine)