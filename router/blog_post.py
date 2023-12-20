from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(prefix='/blog', tags=['blog'])



class Image(BaseModel):
    url: str
    alias: str



class BlogModel(BaseModel):
    pass
    title: str
    content: str
    nb_comment: int
    publisher: Optional[bool]
    tag: List[str]
    metadata: Dict[str, str] = {'key1', 'value1'}
    image: Image = None


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id:int, version:int = 1):
    return {
        'message': 'OK',
        'data': blog,
        'id': id,
        'verion': version
    }


@router.post('/new/{id}/comment/{comment_id}')
def vreate_comment(id:int, blog:BlogModel,
                   comment_title:int = Query(None,
                                          title='text',
                                          description='description',
                                          alias='CommentID',
                                          deprecated=True
                                          ),
                   content:str = Body(
                      Ellipsis,
                       min_length=10,
                       max_length=30,
                       regex='^[A-Z].*'
                   ),
                   v: Optional[List[str]] = Query([1.2, 1.4]),

                   comment_id: int = Path(gt=5)
                   ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id,
    }

