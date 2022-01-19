from mysql import connector
connection=connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='abhi'

)
mycursor=connection.cursor()
sql="INSERT INTO details(name,email,age,user_id) VALUES(%s,%s,%s,%s)"
data=('abhishek','abhi@gmail.com',26,1011)
mycursor.execute(sql,data)
connection.commit()


