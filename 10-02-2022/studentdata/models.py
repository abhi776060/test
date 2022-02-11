
from datbase import Base
from sqlalchemy import Column,String,Integer,Boolean

class Student(Base):
    __tablename__="student"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    sub1=Column(Integer,nullable=False)
    sub2=Column(Integer,nullable=False)
    sub3=Column(Integer,nullable=False)
    sub4=Column(Integer,nullable=True)
    sub5=Column(Integer,nullable=True)
    sub6=Column(Integer,nullable=True)
    status=Column(String)
    chance=Column(Boolean)

