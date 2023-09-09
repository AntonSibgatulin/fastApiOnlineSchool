from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from service.database.database import engine

Base = declarative_base()


class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(600), unique=True, nullable=False)
    user_id = Column(Integer, nullable=False)
