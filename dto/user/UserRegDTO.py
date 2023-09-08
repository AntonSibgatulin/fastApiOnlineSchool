from pydantic import BaseModel


class UserRegDTO(BaseModel):
    name: str
    surname: str
    email: str
    password: str
