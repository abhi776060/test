from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/<name>")
def home1(name):
    return render_template('home.html',text=name)

if __name__=="__main__":
    app.run(debug=True)