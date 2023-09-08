from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:Dert869$$@localhost/online-school"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    print("init_db")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

