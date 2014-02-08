from flask import Flask
from flask import render_template, url_for, redirect,request

app = Flask(__name__)

@app.route("/")
def index():
    if request.method=="GET":
        return render_template("main.html")
    elif request.method=="POST":
        if request.form['button']=="emotion":
            emotion=request.form['emotionvalue']
            return redirect(url_for("results"))

@app.route("/feel")
def results():
    render_template("results.html")

if __name__=="__main__":
    app.debug=True
    app.run(port=8888)
