from fastapi import APIRouter, Depends

import database
from mapper import UserSchema, TokenSchema
from models import User, Token
from repository.user import generate_token
from schemas import UserRegDTO, UserAuthDTO

router = APIRouter(prefix="/api/user", tags=["User"])

get_db = database.get_db


@router.post("/reg")
def reg(userDto: UserRegDTO, db=Depends(get_db)):
    user = User.init(userDto)
    db.add(user)
    db.commit()
    db.refresh(user)

    user_schema = UserSchema()
    result = user_schema.dump(user)
    return result


@router.post("/auth")
def auth(userDto: UserAuthDTO, db=Depends(get_db)):
    user = db.query(User).filter(User.email == userDto.email, User.password == userDto.password).first()
    if user:
        user_schema = UserSchema()
        token_schema = TokenSchema()

        token = Token.init(token=generate_token(user.id), user_id=user.id)
        # saveToken(db, token)
        # set_value(token.token, token.user_id)
        result = user_schema.dump(user)
        result['token'] = token_schema.dump(token)

        return result
    else:
        return {"message": "Not found", "error": 404}
