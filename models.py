from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Double

from schemas import UserRegDTO


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    surname = Column(String(20))
    email = Column(String(100), nullable=False, unique=True)

    password = Column(String(100), nullable=False)
    token = None


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, unique=False, nullable=False, )
    name = Column(String(50), nullable=False)
    description = Column(String(350), nullable=False)
    blog = Column(String(350), nullable=False)
    type = Column(Integer, nullable=True)
    price = Column(Double, nullable=False)
    time = Column(Integer, nullable=False)
    likes = Column(Integer, name="likes", nullable=False, default=0)
    dislikes = Column(Integer, nullable=False, default=0)


class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(600), unique=True, nullable=False)
    user_id = Column(Integer, nullable=False)

    @classmethod
    def init(cls, token, user_id, id=None):
        return cls(id=id, token=token, user_id=user_id)
