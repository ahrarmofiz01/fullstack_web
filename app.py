from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/login",methods=["POST"])
def check_login():
    name=request.form["name"]
    password=request.form["password"]
    if name == "ahrar mofiz" and password=="1234":
        return render_template("success.html",name=name)
    return "in vilide"
