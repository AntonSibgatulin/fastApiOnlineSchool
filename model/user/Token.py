from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from service.database.database import Base


class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(600), unique=True, nullable=False)
    user_id = Column(Integer, nullable=False)

    @classmethod
    def init(cls, token, user_id, id=None):
        return cls(id=id, token=token, user_id=user_id)
