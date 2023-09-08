from fastapi import APIRouter, Depends

from dto.user.UserRegDTO import UserRegDTO

from model.user.User import User
from sqlalchemy.orm import Session

from service.database.database import SessionLocal, init_db

userControllerRouter = APIRouter()


@userControllerRouter.post("/reg")
def reg(userDto: UserRegDTO, db=Depends(init_db)):
    user = User.toUser(userDto)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
