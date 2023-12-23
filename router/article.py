from fastapi import APIRouter, Query, Body, Path, Depends
from pydantic import BaseModel
from typing import Optional, List, Dict
from schemas import ArticleBase, ArticleDisplay, UserBase
from database import db_article
from database.db import get_db
from auth.auth2 import get_current_user



router = APIRouter(prefix='/article', tags=['article'])


# create article
@router.post('/create', response_model=ArticleDisplay)
def create_article(article:ArticleBase, db=Depends(get_db)):
    return db_article.create_article(db, article)


# get one article
@router.get('/get/{id}')
def get_article(id: int, db=Depends(get_db), current_user: UserBase= Depends(get_current_user)):
    return {
        'data': db_article.get_article(id, db),
        'current_user': current_user
    }

