from fastapi import FastAPI, Depends
from controller.UserController import userControllerRouter

from service.database.database import *

import service.redis.redisController

from model.user.User import Base as base_user
from model.user.Token import Base as base_token

base_user.metadata.create_all(bind=engine)
base_token.metadata.create_all(bind=engine)

app = FastAPI(title="Online School")
app.include_router(userControllerRouter, prefix="/api/user", dependencies=[Depends(init_db)])


@app.get("/")
async def root():
    return {"message": "Hello World"}
