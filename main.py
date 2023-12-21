from fastapi import FastAPI, status,Response
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from enum import Enum
from typing import Optional
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import prouct
from database import models
from database.db import engine
from exeptions import EmailNotValid



app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(prouct.router)
models.Base.metadata.create_all(engine)




@app.get('/')
def hello():
    return 'hello world!'


@app.exception_handler(EmailNotValid)
def email_not_valid(request: Request, exe: EmailNotValid):
    return JSONResponse(content=str(exe), status_code=status.HTTP_400_BAD_REQUEST)
