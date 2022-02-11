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
    chance=0
    status='fail'
    if marks >=90:
        chance=3
        status='distinction'
    elif marks >=75 and marks <=90:
        chance=3
        status='average'
    elif marks<=75:
        chance=1
        status="fail"
    return add_student_database(id=id,name=name,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,chance=chance,status=status,db=db,marks=marks)

def update_student_data(id,name,sub1,sub2,sub3,sub4,sub5,sub6,db):
    user=db.query(Student).filter(Student.id==id).first()
    str1=''
    marks=0
    if id == user.id:
        id=id
        name=user.name
        if user.sub1 and user.sub1<75:
            sub1=sub1
        else:
            sub1=user.sub1 
        if user.sub2 and user.sub2<75:
            sub2=sub2
        else:
            sub2=user.sub2
        if user.sub3 and user.sub3<75:
            sub3=sub3
        else:
            sub3=user.sub3
        if user.sub4 and user.sub4<75:
            sub4=sub4
        else:
            sub4=user.sub4
        if user.sub5 and user.sub5<75:
            sub5=sub5
        else:
            sub5=user.sub5
        if user.sub6 and user.sub6<75:
            sub6=sub6
        else:
            sub6=user.sub6

        chance=user.chance
        status="fail"

        if  chance <=3:
            
            if sub4 :
                marks= (sub1+sub2+sub3+sub4)/4
                if sub5:
                    marks=(sub1+sub2+sub3+sub4+sub5)/5
                    if sub6:
                            marks=(sub1+sub2+sub3+sub4+sub5+sub6)/6
            else:
                marks= (sub1+sub2+sub3)/3
        else:
            str1="no more chance "
            return 
        
        status='fail'
        print(marks)
        if marks >=90:
            chance=3
            status='distinction'
        elif marks >=75 and marks <=90:
            chance=3
            status='average'
        elif marks<=75:
            chance=user.chance+1
            status="fail"
        return update_student_database(id=id,name=name,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,chance=chance,status=status,db=db,marks=marks,str1=str1)
    else:
        return f"{id} not present"

def get_id(id,db):
    return get_id_database(id,db)

def remove_id(id,db):
    return remove_id_database(id,db)

def uplod_data(id,name,sub1,sub2,sub3,sub4,sub5,sub6,db):
    return add_student_database(id,name,sub1,sub2,sub3,sub4,sub5,sub6,db)