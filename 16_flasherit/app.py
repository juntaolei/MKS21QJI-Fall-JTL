# Leia Park & Jun Tao Lei
# SoftDev1 pd9
# K#15 -- Do I Know You?
# 2019-10-02

from flask import Flask, session, redirect, url_for, render_template, request
from os import urandom

app = Flask(__name__)

app.secret_key = urandom(32)

# hardcoded username & password:
# FAKE USRNAME
usr = "admin"
# FAKE PASSWORD
passwd = "admin"

# decides whether to redirect to welcome or login page based on session
@app.route("/")
def root():
  if "usr" in session:
    return redirect(url_for("welcome"))
  return redirect(url_for("login"))

# /login checks for form content to match the hardcoded usr info
@app.route("/login", methods = ["GET"])
def login():
  msg = ""
  if request.args:
    # Checks for all inputs to be filled
    if len(request.args["usrname"]) == 0 or len(request.args["passwd"]) == 0:
      msg = "Fill in all the information correctly!"
    # Bad username
    elif request.args["usrname"] != usr:
      msg = "Bad Username!"
    # Bad password
    elif request.args["passwd"] != passwd:
      msg = "Bad Password!"
    # authenticated successfully
    else:
      session["usr"] = request.args["usrname"]
      return redirect(url_for("welcome"))
  return render_template("login.html", msg = msg)

# /welcome renders a template that greets the usr
@app.route("/welcome")
def welcome():
  return render_template("welcome.html", usrname = session["usr"])

# /logout ends the session and redirects to /
@app.route("/logout")
def logout():
  session.pop("usr", None)
  return redirect("/")

if __name__ == "__main__":
  app.run(debug = True)
