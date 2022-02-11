from pydantic import BaseModel


class StudentDetails1(BaseModel):
    id:int
    name:str
    sub1:int
    sub2:int
    sub3:int
class StudentDetails2(BaseModel):
    sub4:int=None
    sub5:int=None
    sub6:int=None
class StudentDetails(StudentDetails1,StudentDetails2):
    pass
 
class EmpBody(BaseModel):
    id:int
    name:str
    status:str
    chance: str
    class Config:
        orm_mode=True
