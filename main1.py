from fastapi import FastAPI
import uvicorn

app=FastAPI()
 
@app.get('/')
def index():
    return {"data":"hai abhishek"}


@app.get('/about')
def index1():
    return {"data":"about"}

if __name__=='__main__':
    uvicorn.run(app)