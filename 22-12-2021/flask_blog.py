from flask import Flask,render_template,request,redirect,url_for,session
from datetime import timedelta

app=Flask(__name__)
app.secret_key='hello'
app.permanent_session_lifetime=timedelta(minutes=5)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =="POST":
        session.permanent=True
        user=request.form['exampleInputEmail1']
        password=request.form['exampleInputPassword1']
        session['email']=user
        session['password']=password
    else:
        if "user" in session:
            return redirect(url_for('details'))
        return render_template('login.html')


@app.route('/details',methods=['POST',"GET"])
def details():
    email=session['email']
    password=session['password']
    



    return render_template('details.html')

if __name__=="__main__":
    app.run(debug=True)