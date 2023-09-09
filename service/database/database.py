from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from model.user import User
from response.user.UserSchema import UserSchema

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


def getUserByEmail(email: str, db: SessionLocal) -> User:
    user = User.query.filter_by(email=email).first()
    if user:
        user_schema = UserSchema()
        result = user_schema.dump(user)
        return result
    else:
        return {"message": "Not found", "error": 404}
