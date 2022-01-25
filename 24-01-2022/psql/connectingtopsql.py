from tkinter.messagebox import NO
import psycopg2
my_bd=None
cur=None
try:
    my_bd=psycopg2.connect(
        host='localhost',
        port="5432",
        database='abhi',
        user='postgres',password='password',

    )
    # print(my_bd)
    cur=my_bd.cursor()
    # querry ='''CREATE TABLE IF NOT EXISTS employee(
    #     id int PRIMARY KEY,
    #     name varchar(40) NOT NULL,
    #     salary float,
    #     dept_id varchar(30))
    #     '''
    # query='INSERT INTO employee (id,name, salary,dept_id) VALUES (%s,%s,%s,%s)'
    # data=[(3,'sachin',15000,'mcs0053'),(2,'karthik',13000,'mcs0086'),]
    # for x in data:

    #     cur.execute(query,x)
    # query='SELECT * FROM employee'
    # query='SELECT id FROM employee'
    # query='SELECT name FROM employee'
    query='SELECT * FROM employee'

    cur.execute(query)
    result=cur.fetchall()
    for x in result:
        print(x)
    # my_bd.commit()
    # update_query='UPDATE employee SET salary = salary + (salary*0.5) '
    # cur.execute(update_query)
    # my_bd.commit()
    del_query='DELETE from employee WHERE id=1'
    cur.execute(del_query)
    my_bd.commit()
except Exception as e:
    print('error',e)
finally:
    if cur is not None:
        cur.close()
        my_bd.close()