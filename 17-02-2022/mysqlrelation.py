from mysql import connector

mydb=connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='bank',
)
cur=mydb.cursor()
query1='''create table emplooyee(eid int primary key,
ename varchar(255),
esal int)'''
query2=''' select * from emplooyee'''
query3=''' desc emplooyee'''
cur.execute(query3)
var=cur.fetchall()
print(var)
