from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Строка подключения с учетом порта 5433 и твоей базы jobcraft
DATABASE_URL = "postgresql+psycopg2://postgres:elzat_2006@localhost:5433/jobcraft"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass