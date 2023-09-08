from fastapi import FastAPI, Depends
from controller.UserController import userControllerRouter

from service.database.database import  init_db




app = FastAPI(title="Online School")
app.include_router(userControllerRouter, prefix="/api/user", dependencies=[Depends(init_db)])





@app.get("/")
async def root():
    return {"message": "Hello World"}
