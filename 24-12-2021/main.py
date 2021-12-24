from flask import Flask,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


app=Flask(__name__)
app.secret_key='abhi'
app.permanent_session_lifetime=timedelta(minutes=5)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///./user.db'
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db=SQLAlchemy(app)

class User(db.Model):
    email=db.Column(db.Integer,primary_key=True)
    password=db.Column(db.String)

class Log(User):
    email = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)
    c_password = db.Column(db.String)

class details(db.Model):
    f_name=db.Column(db.String)
    l_name = db.Column(db.String)
    age=db.Column(db.Integer)
    sex=db.Column(db.String)

@app.route('/')
@app.route('/myshop')
def myshop():
    return render_template("myshop.html")


@app.route('/login', methods=["POST","GET"])
def login():
    if request.method=="POST":
        email=request.form['email']
        password = request.form['password']
        session.permanent=True
        session['email']=email
        session['password'] = password

    return render_template("login.html")

if __name__=='__main__':
    app.run(debug=True)
