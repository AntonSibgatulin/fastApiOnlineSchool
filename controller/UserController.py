from fastapi import APIRouter, Depends

from dto.user.UserAuthDTO import UserAuthDTO
from dto.user.UserRegDTO import UserRegDTO

from model.user.User import User
from sqlalchemy.orm import Session

from response.user.UserSchema import UserSchema
from service.database.database import SessionLocal, init_db
import service.redis.redisController
userControllerRouter = APIRouter()


@userControllerRouter.post("/reg")
def reg(userDto: UserRegDTO, db=Depends(init_db)):
    user = User.toUser(userDto)
    db.add(user)
    db.commit()
    db.refresh(user)

    user_schema = UserSchema()
    result = user_schema.dump(user)
    return result


@userControllerRouter.post("/auth")
def auth(userDto: UserAuthDTO, db=Depends(init_db)):
    user = db.query(User).filter(User.email == userDto.email, User.password == userDto.password).first()
    if user:
        user_schema = UserSchema()
        result = user_schema.dump(user)
        return result
    else:
        return {"message": "Not found", "error": 404}
