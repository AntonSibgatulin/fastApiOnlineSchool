from fastapi import APIRouter, Depends

from dto.user.UserAuthDTO import UserAuthDTO
from dto.user.UserRegDTO import UserRegDTO
from model.user.Token import Token

from model.user.User import User
from sqlalchemy.orm import Session

from response.user.UserSchema import UserSchema, TokenSchema
from service.database.database import SessionLocal, init_db

from service.token.tokenService import *

from service.redis.redisController import *

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
        token_schema = TokenSchema()

        token = Token.init(token=generate_token(user.id), user_id=user.id)
        # saveToken(db, token)
        set_value(token.token, token.user_id)
        result = user_schema.dump(user)
        result['token'] = token_schema.dump(token)

        return result
    else:
        return {"message": "Not found", "error": 404}


'''
def saveToken(db: SessionLocal, token: Token) -> Token:
    db.add(token)
    db.commit()
    db.refresh(token)
    return token
'''
