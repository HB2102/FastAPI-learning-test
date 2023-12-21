from fastapi import FastAPI, status,Response
from enum import Enum
from typing import Optional
from router import blog_get
from router import blog_post
from router import user
from router import article
from database import models
from database.db import engine



app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
models.Base.metadata.create_all(engine)




@app.get('/')
def hello():
    return 'hello world!'




