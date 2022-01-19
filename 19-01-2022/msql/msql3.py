from mysql import connector
connection=connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='abhi'

)
mycursor=connection.cursor()
sql="show tables"
mycursor.execute(sql)
# for table in mycursor:
#     print(table)
name=mycursor.fetchall()
print(name)

