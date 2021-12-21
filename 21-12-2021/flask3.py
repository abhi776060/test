from flask import  Flask,render_template,request,redirect,url_for,session,flash
from datetime import timedelta

app= Flask(__name__)
app.secret_key='abhi'
app.permanent_session_lifetime=timedelta(minutes=5)

@app.route('/')
def home():
    return render_template("home3.html")

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        session.permanent=True
        name=request.form['nme']
        flash("login")
        session['name']=name
        return redirect(url_for("user"))
    else:
        if 'name' in session:
            return redirect(url_for('user'))
        return render_template('home4.html')
@app.route('/user')
def user():
    if "name" in session:
        name=session['name']
        return f"{name} successfully "
    else:
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session.pop('name',None)
    flash('logout successful')
    return redirect(url_for('login'))



if __name__=='__main__':
    app.run(debug=True)
