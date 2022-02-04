from mysql import connector

server=connector.connect(
    host='localhost',
    # port=5432,
    user='root',
    passwd='password',
    database='number',
)
# print(server)

def create_table(arg):
    server1=server
    query=f'''create table {arg} (message string(5000))'''
    cur=server1.cursor()
    cur.execute(query)
create_table('7760607275')

