from flask import Flask, render_template
import datetime

app = Flask(__name__)
#index page
@app.route("/")
def index():
    return "Hello Dazi"

@app.route("/lol")
def lol():
    return "kkk"

# @app.route("/<string:name>")
# def name(name):
#     name = name.capitalize()
#     return "Hello " + name

# @app.route("/<string:day>")
# def isitfriday(day):
#     day = day.capitalize()
#     day1 = datetime.datetime.now()
#     if day1.strftime("%A") == day:
#         return "yes"
#     else:
#         return "No"

@app.route("/hellov2<string:name>")
def hello(name):
    return render_template("hello.html", name = name)
