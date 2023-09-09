from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from model.user import User
from response.user.UserSchema import UserSchema

DATABASE_URL = "mysql+mysqlconnector://root:Dert869$$@localhost/online-school"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    print("init_db")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
