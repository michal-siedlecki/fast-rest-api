from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseModel = declarative_base()
