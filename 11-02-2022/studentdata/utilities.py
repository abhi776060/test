from audioop import avg
from datbase import SessionLocal
import models,schemas
def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()
def add_student_database(id,name,marks,sub1,sub2,sub3,status,db,chance,sub4=None,sub5=None,sub6=None):
    try:
        new_user=models.Student(id=id,name=name,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,status=status,chance=chance,avr=marks)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return "data added succefully"
    except Exception as e:
        pass

def update_student_database(id,name,sub1,sub2,sub3,sub4,sub5,sub6,chance,status,db,marks,str1):
    str2=''
    if str1:
        str2=str1
    else:
        str2="data added succefully"

    if id:
        new_user=db.query(models.Student).filter(models.Student.id==id).first()
        print('hai')
        new_user.sub1=sub1
        new_user.sub2=sub2
        new_user.sub3=sub3
        new_user.sub4=sub4
        new_user.sub5=sub5
        new_user.sub6=sub6
        new_user.status=status
        new_user.chance=chance
        new_user.avr=marks
        db.add(new_user)
        db.commit()
        return f"{str2}"
    else:
        return "data insertion failed"
def get_id_database(id,db):
    try:
        user=db.query(models.Student).filter(models.Student.id==id).first()
        print('..............',user)
        if user.id != None:
            print('......from if ........',user)
            return user
        else:
            print('.......from else.......',user)
            return "please verify id "
        
    except:
        return "please verify id "

def remove_id_database(id,db):
    user=db.query(models.Student).filter(models.Student.id==id).delete()
    if user:
        db.commit()
        return f" {id} deleted succefully"
    else:
        return f'{id} not present '

    