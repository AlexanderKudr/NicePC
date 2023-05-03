from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = 'postgresql://kotatsu:qwerty@45.87.246.48:5432/nicepc_psql'
SQLALCHEMY_DATABASE_URL = 'postgresql://pstmjrmx:CnwDwhLyL5V4eB-Htw4evy87LeGAE8cF@balarama.db.elephantsql.com/pstmjrmx'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()