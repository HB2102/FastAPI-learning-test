from fastapi import APIRouter, Response,status
from typing import Optional




router = APIRouter(prefix='/blog', tags=['blog'])

@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid:bool=True, username: Optional[str]=None):
    return {'message': f"blog is {id} comment id {comment_id} {valid=} {username=}"}


@router.get('/all')
def get_blogs(page:Optional[int]=None, page_size:Optional[str]=None):
    return {'message': f'{page=} -- {page_size=}'}



@router.get('/{id}', status_code=status.HTTP_200_OK, summary='blog input',
         response_description="all blog we have")
def get_blog(id:int, response:Response):
    if id > 5:
        response.status_code= status.HTTP_404_NOT_FOUND
        return {'Error': f"Blog {id} Not Found !"}
    return {'message': f'blogs {id}'}
