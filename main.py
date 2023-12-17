from fastapi import FastAPI
from enum import Enum


app = FastAPI()


@app.get('/')
def hello():
    return 'hello world!'



class TypeBlogs(str,Enum):
    M1 = 'mesal 1'
    M2 = 'mesal 2'
    M3 = 'mesal 3'

@app.get('/blog/type/{type}')
def get_type_blog(type:TypeBlogs):
    return {'message': f'blog type in {type}'}


@app.get('/blog/all')
def get_blogs():
    return {'message': f'all blogs'}



@app.get('/blog/{id}')
def get_blog(id:int):
    return {'message': f'blogs {id}'}



