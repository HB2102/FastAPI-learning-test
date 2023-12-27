import time

from fastapi import FastAPI, status, Response
from fastapi.requests import Request
from fastapi.responses import JSONResponse, HTMLResponse
from router import blog_get, blog_post, user, article, prouct, file
from database import models
from database.db import engine
from exeptions import EmailNotValid
from auth import authentication
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocket
from client import html



app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(prouct.router)
app.include_router(authentication.router)
app.include_router(file.router)
models.Base.metadata.create_all(engine)

app.mount('/files', StaticFiles(directory='files'), name='files')


origins = [
    'https://www.google.com',
    ['*'],
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)



clients = []

@app.websocket('/chat')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for client in clients:
            await client.send_text(data)


@app.get('/')
def get_websocket():
    return HTMLResponse(html)






@app.exception_handler(EmailNotValid)
def email_not_valid(request: Request, exe: EmailNotValid):
    return JSONResponse(content=str(exe), status_code=status.HTTP_400_BAD_REQUEST)



@app.middleware('http')
async def add_middle_ware(request: Request, call_next):
    print('before call')
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    # print(response.headers)
    response.headers['dueation'] = str(duration)
    print('after call')
    return response
