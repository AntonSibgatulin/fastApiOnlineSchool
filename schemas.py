from pydantic import BaseModel


class UserAuthDTO(BaseModel):
    email: str
    password: str


class UserRegDTO(BaseModel):
    name: str
    surname: str
    email: str
    password: str
