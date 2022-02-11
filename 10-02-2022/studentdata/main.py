from fastapi import FastAPI,Depends
from typing import List
import uvicorn
from schemas import StudentDetails,StudentDetails1,StudentDetails2,EmpBody


from utilities import get_db
from views import add_student_data,update_student_data,get_id,remove_id
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
    sub4=e.sub4
    sub5=e.sub5
    sub6=e.sub6
    return update_student_data(id,sub4,sub5,sub6,db)

@app.get('/get-by-id',response_model=EmpBody)
def fetch(id:int,db:Session = Depends(get_db)):
    return get_id(id,db)

@app.delete('/remove-student-id')
def remove(id:int,db:Session = Depends(get_db)):
    return remove_id(id,db)



if __name__=="__main__":
    uvicorn.run(app,debug=True)
