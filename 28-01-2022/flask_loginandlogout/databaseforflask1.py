from mysql import connector

def connect_database_mcs():
    my_db=connector.connect(
        host="localhost",
        user="root",
        passwd='password',
        database='mcs',
    )
    return my_db

server=connect_database_mcs()
cur=server.cursor()
# sql='''create table employee (username varchar(25),fname varchar(25), lname varchar(25), email varchar(50),pass1 int,pass2 int)'''
# sql=''' insert into employee (username,fname,lname,email,pass1,pass2) values(%s,%s,%s,%s,%s,%s)'''
# data=('abhishek0088','abhishek','k s','abhigaja08@gmail.com','123','123')
# cur.execute(sql,data)
# server.commit()






# def create_database(databasename):
#     database=my_server()
#     cur=database.cursor()
#     sql=f'create database {databasename}'
#     return cur.execute(sql)
# # create_database('abhishek')

# def active_database(databasename):
#     my_db=connector.connect(
#         host="localhost",
#         user="root",
#         passwd='password',
#         database=f'{databasename}',
#     )
#     return my_db
# # active_database('abhishek')










