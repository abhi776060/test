from flask import Flask,render_template,request,redirect,url_for,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.secret_key='hello'
app.permanent_session_lifetime=timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)
class User(db.Model):
    university_num=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    email = db.Column(db.String)
    address = db.Column(db.String)
    country = db.Column(db.String)
    gender = db.Column(db.String)
    def __init__(self,university_num=None,name=None,email=None,address=None,country=None,gender=None):
        self.university_num=university_num
        self.name=name
        self.email=email
        self.address=address
        self.country=country
        self.gender=gender
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/signin',methods=['POST','GET'])
# def signin():
#     if request.method =="POST":
#         session.permanent=True
#         university_num = request.form['university_num']
#         name=request.form['name']
#         email=request.form['email']
#         address = request.form['address']
#         country = request.form['country']
#         gender = request.form['gender']
#         session['university_num']=university_num
#
#
#         return redirect(url_for('details'))
#     # else:
#     #     if "user" in session:
#     #         email=session['email']
#     #         return redirect(url_for('details'))
#     #     else:
#     #         return redirect('login')
#     return render_template('login.html')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        session.permanent=True
        university_num = request.form['university_num']
        name=request.form['name']
        email=request.form['email']
        address = request.form['address']
        country = request.form['country']
        gender = request.form['gender']
        session['university_num']=university_num
        user=User.query.filter_by(university_num=university_num).first()
        if user  :
            flash("user already exit")
            return redirect(url_for("details"))

        else:
            user=User(university_num,name,email,address,country,gender)
            db.session.add(user)
            db.session.commit()
            flash('successful')

            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/details',methods=['POST',"GET"])
def details():
    session['university_num']=112233
    if "university_num" in session:
        university_num=session['university_num']
        user=User.query.filter_by(university_num=university_num).all()
        return "jgsb"
    return redirect(url_for('home'))


if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
