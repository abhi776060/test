from mysql import connector
connection=connector.connect(
    host='localhost',
    user='root',
    passwd='password',
)
mycursor=connection.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)

