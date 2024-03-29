import time

from fastapi import APIRouter, Response, Header, Cookie, Form
from fastapi.responses import HTMLResponse, PlainTextResponse, Response



router = APIRouter(prefix='/product', tags=['product'])

products = ['watch', 'clock', 'microphone']



async def test_acync():
    time.sleep(10)
    return 'ok'





@router.get('/')
async def get_all():
    await test_acync()
    data = " ".join(products)
    response = Response(content=data, media_type='text/plain')
    response.set_cookie(key='cookie', value='test')
    return response


@router.post('/create')
def create_product(data: str=Form(...)):
    products.append(data)
    return products






@router.get('/withheader')
def get_product(custom_header: str = Header(None),
                cookie: str = Cookie(None)):
    print(custom_header)
    print(cookie)
    return {'data':products, 'header': custom_header, 'cookie': cookie}




@router.get('/{id}', responses={
    404: {'content': {'text/plain': {
        'example': "product not found"
    }},
        'description': 'when product not found'
    },
    200: {'content': {'text/html': {
        'example': "<div> {data} </div>"
    }},
        'description': 'Html Code Data'
    }

})
def get_product(id: int):
    if id > len(products):
        text = "prouct not found"
        return PlainTextResponse(content=text, media_type='text/plain')

    data = products[id]
    return HTMLResponse(content=f'<div> {data} </div>', media_type='text/html')
