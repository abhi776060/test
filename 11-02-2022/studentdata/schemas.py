from pydantic import BaseModel
from typing import Optional

class StudentDetails1(BaseModel):
    id:int
    name:str
    
class StudentDetails2(BaseModel):
    sub1:int
    sub2:int
    sub3:int
    sub4:int=None
    sub5:int=None
    sub6:int=None
class StudentDetails(StudentDetails1,StudentDetails2):
    pass
 
class EmpBody(BaseModel):
    id:Optional[int]
    name:Optional[str]
    status:Optional[str]
    avr:Optional[float]
    class Config:
        orm_mode=True
