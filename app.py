from flask import Flask
from flask import render_template, url_for, redirect,request
import tweetSentiment

app = Flask(__name__)

@app.route("/")
def index():
    if request.method=="GET":
        return render_template("main.html")
    elif request.method=="POST":
        print request.form['button']
        if request.form['button']=="emotion":
            emotion=request.form['emotionvalue']
            positive=tweetSentiment.getPositive(emotion)
            percent=tweetSentiment.getConfidence(emotion)
            print "here"
            return render_template("main.html",positive=positive,confidence=percent,answer=True)

@app.route("/results")
def results():
    return render_template("main.html",)

if __name__=="__main__":
    app.debug=True
    app.run(port=8888)
