from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional


router = APIRouter(prefix='/blog', tags=['blog'])



class BlogModel(BaseModel):
    pass
    title:str
    content:str
    nb_comment:int
    publisher:Optional[bool]


@router.post('/new')
def create_blog(blog: BlogModel):
    return {
        'message': 'OK',
        'data': blog,
    }