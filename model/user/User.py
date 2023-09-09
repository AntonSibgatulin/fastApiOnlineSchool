from sqlalchemy import Column, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from dto.user.UserRegDTO import UserRegDTO
from service.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    surname = Column(String(20))
    email = Column(String(100), nullable=False, unique=True)

    password = Column(String(100), nullable=False)
    token = None

    @classmethod
    def toUser(cls, userDTO: UserRegDTO):
        return cls(id=None, name=userDTO.name, surname=userDTO.surname, email=userDTO.email, password=userDTO.password)
