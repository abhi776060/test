from flask import Flask,render_template

app=Flask(__name__)

# @app.route('/')
# def home():
#
#     return {1: 'apple',2: 'banana', 3: 'carrot'}

@app.route('/')
def home():
    items={1:'apple',2:'banana',3:'carrot'}
    return render_template("home.html",text=items)

if __name__=="__main__":
    app.run(debug=True)