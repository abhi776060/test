from mysql import connector
connection=connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='abhi'

)
mycursor=connection.cursor()
sql='DELETE FROM details WHERE user_id=1011'

mycursor.execute(sql)
connection.commit()


