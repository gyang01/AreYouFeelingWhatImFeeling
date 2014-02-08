from flask import Flask
from flask import render_template, url_for, redirect,request
import urllib2,json
import utils

app = Flask(__name__)

@app.route("/")
def index():
    render_template("main")

if __name__=="__main__":
    app.debug=True
    app.run(port=8888)
