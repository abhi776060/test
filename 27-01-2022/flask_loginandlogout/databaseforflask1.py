from mysql import connector

def my_server():
    my_db=connector.connect(
        host="localhost",
        user="root",
        passwd='password',
    )
    return my_db

def create_database(databasename):
    database=my_server()
    cur=database.cursor()
    sql=f'create database {databasename}'
    return cur.execute(sql)
# create_database('abhishek')

def active_database(databasename):
    my_db=connector.connect(
        host="localhost",
        user="root",
        passwd='password',
        database=f'{databasename}',
    )
    return my_db
# active_database('abhishek')








