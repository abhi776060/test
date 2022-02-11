from fastapi import FastAPI,Depends,UploadFile
from typing import List
import uvicorn
from schemas import StudentDetails,StudentDetails1,StudentDetails2,EmpBody


from utilities import get_db
from views import add_student_data,update_student_data,get_id,remove_id,uplod_data
from datbase import engine
import models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


app=FastAPI()

@app.post('/add-student-details')
def add_student(e:StudentDetails,db:Session = Depends(get_db)):
    try:
        id=e.id
        name=e.name
        sub1=e.sub1
        sub2=e.sub2
        sub3=e.sub3
        sub4=e.sub4
        sub5=e.sub5
        sub6=e.sub6
        
        return add_student_data(id,name,sub1,sub2,sub3,sub4,sub5,sub6,db)
    except:
        return "some data missing please provide"

@app.put('/take-a-chance')
def alter(id:int,e:StudentDetails2,db:Session = Depends(get_db)):
    id=e.id
    name=e.name
    sub1=e.sub1
    sub2=e.sub2
    sub3=e.sub3
    sub4=e.sub4
    sub5=e.sub5
    sub6=e.sub6
    return update_student_data(id,name,sub1,sub2,sub3,sub4,sub5,sub6,db)

@app.get('/get-by-id',response_model=EmpBody)
def fetch(id:int,db:Session = Depends(get_db)):
    return get_id(id,db)

@app.delete('/remove-student-id')
def remove(id:int,db:Session = Depends(get_db)):
    return remove_id(id,db)

@app.post('/csvfile-upload')
def cvs_loader(f:UploadFile,db:Session = Depends(get_db)):
    dict1=[]
    encode='utf-8'
    str1=f.file.read().decode(encode)
    for x in str1.split('\r\n'):
        dict1.append(x)
    # list1=str1.split(',') 
    list1=[]
    for x in dict1:
        if x:
            list1.append(x.split(','))
    for x in list1:
        if x[0]:
            id=int(x[0])
        else:
            id=1
        if x[1]:
            name=x[1]
        else:
            name=''
        if x[2]:
            sub1=int(x[2])
        else:
            sub1=0
        if x[3]:
            sub2=int(x[3])
        else:
            sub2=0
        if x[4]:
            sub3=int(x[4])
        else:
            sub3=0
        if x[5]:
            sub4=int(x[5])
        else:
            sub4=0
        if x[6]:
            sub5=int(x[6])
        else:
            sub5=0
        if x[7]:
            sub6=int(x[7])
        else:
            sub6=0
        add_student_data(id,name,sub1,sub2,sub3,sub4,sub5,sub6,db)
    return list1

    



if __name__=="__main__":
    uvicorn.run(app,debug=True)
