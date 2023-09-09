from models.user.User import User
from service.database.database import SessionLocal

import service.redis.redisController as Redis


def getUserByToken(token: str, db: SessionLocal) -> User:
    id = Redis.get_value(token)
    if id is None:
        return None
    return db.query(User).filter(User.id == int(id)).first()
