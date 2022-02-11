from datbase import SessionLocal
import models,schemas

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()
def add_student_database(id,name,sub1,sub2,sub3,chance,status,db,sub4=None,sub5=None,sub6=None):
    try:
        new_user=models.Student(id=id,name=name,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,chance=chance,status=status)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return "data added succefully"
    except:
        return "data not inserted"

def update_student_database(id,name,sub1,sub2,sub3,sub4,sub5,sub6,chance,status,db):
    if id:
        new_user=db.query(models.Student).filter(models.Student.id==id).first()
        
        new_user.sub4=sub4
        new_user.sub5=sub5
        new_user.sub6=sub6
        new_user.chance=chance
        new_user.status=status
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return "data added succefully"
    else:
        return "data not inserted"
def get_id_database(id,db):
    user=db.query(models.Student).filter(models.Student.id==id).first()
    if user:
        return user
    else:
        return "please verify id "

def remove_id_database(id,db):
    user=db.query(models.Student).filter(models.Student.id==id).delete()
    if user:
        db.commit()
        return f" {id} deleted succefully"
    else:
        return f'{id} not present '

    