import os
import json
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

from helpers import hira, kata, shuffler, quiz, word_incr
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index ():
    return render_template("/index.html")

# All routes related to Hiragana track
@app.route("/hiragana/", methods=["GET", "POST"])
def hiragana ():
    words = word_incr()
    temp = hira()
    groups = len(temp)
    return render_template("/hiragana.html", groups=groups, words=words)

@app.route("/hiragana/learner", methods=["GET", "POST"])
def hirafirst ():
    if request.method=="POST":
        d = request.form.get("group")
        x = int(d)
        temp = hira()
        if x >= len(temp) or x < 0:
            return hiragana()
        keys = []
        values = []
        for i in temp[x]:
            for key, value in i.items():
                keys.append(key)
                values.append(value)
        y = len(keys)
        return render_template("/learner.html", y=y, x=x, values=values, keys=keys, d=d)
    else:
        return render_template('/learner.html')
#All routes related to Katakana track
@app.route("/katakana/", methods=["GET", "POST"])
def katakana ():
    words = word_incr()
    temp = kata()
    groups = len(temp)
    return render_template("/katakana.html", groups=groups, words=words)

@app.route("/katakana/learner", methods=["GET", "POST"])
def katafirst ():
    if request.method == "POST":
        id = 2
        d = request.form.get("group")
        x = int(d)
        temp = kata()
        if x >= len(temp) or x < 0:
            return katakana()
        keys = []
        values = []
        for i in temp[x]:
            for key, value in i.items():
                keys.append(key)
                values.append(value)
        y = len(keys)
        return render_template("learner.html", y=y, x=x, values=values, keys=keys, d=d, id=id)

@app.route("/quizzer", methods=["GET", "POST"])
def quizzer ():
    
        return render_template("quizzer.html")
if __name__== "__main__":
    app.run(debug=True)

def shuffler(list):
    list = hira()
    groups = input("Enter an integer: ")
    if int(groups) == ValueError:
        print ('Input invalid, please try again.  Input must be an integer.')
        return None
    else:
        number = int(groups)
        if number > len(list):
            print ('Number must be less than', len(list))
            return None
        newlist= []
        for i in range(number):
            random.shuffle(list[i])
            newlist += list[i]
        random.shuffle(newlist)
        return newlist

def shuffler(list):
    list = hira()
    groups = input("Enter an integer: ")
    if int(groups) == ValueError:
        print ('Input invalid, please try again.  Input must be an integer.')
        return None
    else:
        number = int(groups)
        if number > len(list):
            print ('Number must be less than', len(list))
            return None
        newlist= []
        for i in range(number):
            random.shuffle(list[i])
            newlist += list[i]
        random.shuffle(newlist)
        return newlist
