import psycopg2

mydatabase = psycopg2.connect(host="localhost",
                        port="5432",
                        user="postgres",

                        password="password")



cursor1 = mydatabase.cursor()



query = "CREATE DATABASE student"


cursor1.execute(query)