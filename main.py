from fastapi import FastAPI

import routers.user
from database import engine

import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online School")
app.include_router(router=routers.user.router)


@app.get("/")
async def root():
    return {"message": "Hello world", "description": "", "name": ""}
