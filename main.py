from pyexpat import model

from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer

from controller.ArticleController import article_router
from controller.UserController import userControllerRouter

from service.database.database import Base, engine, init_db
from service.security.securityService import get_token

model.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Online School")
security = HTTPBearer()
app.include_router(userControllerRouter, prefix="/api/user", dependencies=[Depends(init_db), Depends(get_token)])
app.include_router(article_router, prefix="/api/article", dependencies=[Depends(init_db), Depends(get_token)])


@app.get("/")
async def root():
    return {"message": "Hello world", "description": "", "name": ""}
