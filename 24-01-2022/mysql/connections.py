from mysql import connector
try:
    # my_db=connector.connect(
    #     host='localhost',
    #     user='root',
    #     passwd='password',
    # )
    my_db=connector.connect(
        host='localhost',
        user='root',
        passwd='password',
        database='mcs',
    )
    cur=my_db.cursor()
    # sql='create database mcs'
    # sql='create table employee(name varchar(20),emid varchar(20),email varchar(20),adress varchar(20))'
    sql='insert into employee(name,emid ,email ,adress ) values (%s,%s,%s,%s)'
    data=('abhishek','mcs0094','abhishek@gmail.com', 'kyathanahalli')
    cur.execute(sql,data)
    my_db.commit()
except Exception as e:
    print(e)