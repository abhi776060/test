from utilities import add_student_database,update_student_database,get_id_database,remove_id_database
from models import Student

def add_student_data(id,name,sub1,sub2,sub3,sub4,sub5,sub6,db):
    marks=0
    if sub4 :
       marks= (sub1+sub2+sub3+sub4)/4
       if sub5:
            marks=(sub1+sub2+sub3+sub4+sub5)/5
            if sub6:
                marks=(sub1+sub2+sub3+sub4+sub5+sub6)/6
    else:
       marks= (sub1+sub2+sub3)/3
    chance=False
    status='fail'
    if marks >=90:
        chance=False
        status='distinction'
    elif marks >=75 and marks <=90:
        chance=False
        status='average'
    elif marks<=75:
        chance=True
        status="fail"
    return add_student_database(id=id,name=name,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,chance=chance,status=status,db=db)

def update_student_data(id,sub4,sub5,sub6,db):
    user=db.query(Student).filter(Student.id==id).first()
    if id == user.id:
        id=id
        name=user.name
        sub1=user.sub1
        sub2=user.sub2
        sub3=user.sub3
        sub4=sub4
        sub5=sub5
        sub6=sub6
        status="fail"
        chance=False
        if  status:
            marks=0
            if sub4 :
                marks= (sub1+sub2+sub3+sub4)/4
                if sub5:
                    marks=(sub1+sub2+sub3+sub4+sub5)/5
                    if sub6:
                            marks=(sub1+sub2+sub3+sub4+sub5+sub6)/6
        else:
             marks= (sub1+sub2+sub3)/3
        chance=False
        status='fail'
        if marks >=90:
            chance=False
            status='distinction'
        elif marks >=75 and marks <=90:
            chance=False
            status='average'
        elif marks<=75:
            chance=True
            status="fail"
        return update_student_database(id=id,name=name,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,chance=chance,status=status,db=db)
    else:
        return f"{id} not present"

def get_id(id,db):
    return get_id_database(id,db)

def remove_id(id,db):
    return remove_id_database(id,db)