from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.app.utilities.config import dbConfig

DB_URL = f"mysql+pymysql://{dbConfig.user}:{dbConfig.password}@localhost:3306/{dbConfig.name}"
print(DB_URL)
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close() 