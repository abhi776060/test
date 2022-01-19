from mysql import connector
connection=connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='sakila'
)
mycursor=connection.cursor()
mycursor.execute("select * from actor ")

'''
for x in mycursor:
    print(x)

'''
result=mycursor.fetchall()
print(result)
