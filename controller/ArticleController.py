from fastapi import APIRouter, Depends

from service.database.database import init_db
from service.security.securityService import get_token
from service.database.database_helper import *

article_router = APIRouter()


@article_router.get("/get")
def get(token: tuple = Depends(get_token), db=Depends(init_db)):
    user = getUserByToken(token, db)
    if user:

        pass
    else:
        pass

    return {"message": "Hello World"}
