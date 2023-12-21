from fastapi import APIRouter, Query, Body, Path, Depends
from pydantic import BaseModel
from typing import Optional, List, Dict
from schemas import ArticleBase, ArticleDisplay
from database import db_article
from database.db import get_db



router = APIRouter(prefix='/article', tags=['article'])


# create article
@router.post('/create', response_model=ArticleDisplay)
def create_article(article:ArticleBase, db=Depends(get_db)):
    return db_article.create_article(db, article)


# get one article
@router.get('/get/{id}', response_model=ArticleDisplay)
def get_article(id: int, db=Depends(get_db)):
    return db_article.get_article(id, db)

