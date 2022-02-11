
from datbase import Base
from sqlalchemy import Column,String,Integer,Float

class Student(Base):
    __tablename__="student"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    sub1=Column(Integer,nullable=True)
    sub2=Column(Integer,nullable=True)
    sub3=Column(Integer,nullable=True)
    sub4=Column(Integer,nullable=True)
    sub5=Column(Integer,nullable=True)
    sub6=Column(Integer,nullable=True)
    status=Column(String)
    chance=Column(Integer)
    avr=Column(Float)

