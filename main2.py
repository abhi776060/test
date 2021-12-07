from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get('/')
def index():
    return {'data':'my first data'}

@app.get('/{id}')
def sub_index(id:int):
    return 'my id:{}'.format(id)
