from os import name
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app=FastAPI()
students={
    1:{'name':'abhishek',
    'age':25,
    'year':'12th stnd'}
}
class Students(BaseModel):
    name:str
    age:int
    year:str
class Update(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[str]=None
@app.get('/')
def index():
    return {'name':'first api'}

@app.get('/get_student/{id}')
def get_student(id:int):
    if id in students:
        return students[id]
    return {"message":f"Sorry {id} is present"}

@app.get('/get_student_name/{id}')
def get_name(name:str,id:int):
    for x in students.keys():
        if students[x]['name']==name:
            return students[x]
    return {"message":f"no {name} and {name}'s key not present"}

@app.post('/studen_create/{id}')
def create(id:int,request:Students):
    if id in students:
        return {'Error':f'{id} is already present'}
    students[id]=request
    return { id:request}

@app.put('/student_update/{id}')
def student_update(id:int,update:Update):
    if id not in  students:
        return {'Error':'no key found in students'}
    if update.name!=None:
        students[id]['name']=update.name
    if update.age!=None:
        students[id]['age']=update.age
    if update.year!=None:
        students[id]['year']=update.year
    return {id:update[id]}
@app.delete('/data_delete/{id}')
def destroy(id:int):
    if id not in students:
        return {"Error":f'{id} not present'}
    del students[id]
    return{f'{id} deleted':'Sucessful'} 