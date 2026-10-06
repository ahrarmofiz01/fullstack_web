from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return"you are on flask server"
@app.route("/about")
def about():
    return "this is about page"
