from flask import Flask,render_template,request,redirect
from databaseforflask1 import connect_database_mcs

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home1():
    return render_template('index.html')

@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('index.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    
    if request.method =='POST':
        username= request.form['username']
        fname= request.form['fname']
        lname= request.form['lname']
        email= request.form['email']
        pass1= request.form['pass1']
        pass2= request.form['pass2']
        
        server=connect_database_mcs()
        cur=server.cursor()
        sql='select username from employee'
        cur.execute(sql)
        
        obj=cur.fetchall()
        print(obj)
        if pass1==pass2:
            if username not in obj:
                sql=''' insert into employee (username,fname,lname,email,pass1,pass2) values(%s,%s,%s,%s,%s,%s)'''
                data=(username,fname,lname,email,pass1,pass2)
                cur.execute(sql,data)
                server.commit()
                return redirect('home')
            else:
                print("user alraedy there")
        else:
            print('password wrong')

            

        



    return render_template('signup.html')


if __name__=='__main__':
    app.run(debug=True)