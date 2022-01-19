from mysql import connector
connection=connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='abhi'

)
mycursor=connection.cursor()
sql="create table details (name VARCHAR(50),email VARCHAR(25),age INTEGER(10),user_id INTEGER AUTO_INCREMENT PRIMARY KEY)"
mycursor.execute(sql)


