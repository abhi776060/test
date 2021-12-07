from fastapi import FastAPI
import uvicorn

app=FastAPI()


@app.get('/')
def index():
    return 'hello abhishek'


@app.get('/item/{item_id}')
def show(item_id:int):
    return {'page':item_id}

@app.put('/item/{item_id}')
def show(item_id:int):
    return {'page':item_id}

