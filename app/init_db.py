from app.database_config import engine
from app.models import Base

Base.metadata.create_all(bind=engine)