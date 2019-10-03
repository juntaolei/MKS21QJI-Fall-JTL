# Team Blorb: Leia Park & Jun Tao Lei
# SoftDev1 pd9
# K#15 -- Do I Know You?
# 2019-10-02

from flask import Flask, session, redirect, url_for, render_template, request
from os import urandom

app = Flask(__name__)

app.secret_key = urandom(32)

# FAKE USRNAME
usr = "admin"
# FAKE PASSWORD
passwd = "admin"

# / decides whether to redirect to welcome or login page based on session
@app.route("/")
def root():
  if "usr" in session:
    return redirect(url_for("welcome"))
  return redirect(url_for("login"))

# /login checks for form content to match the hardcoded usr info
@app.route("/login", methods = ["GET"])
def login(msg = ""):
  if request.args:
    if not bool(request.args["usrname"]) or not bool(request.args["passwd"]): # Checks for all inputs to be filled
      msg = "Fill in all the information correctly!"
    else:
      msg = ["","Bad Username! "][request.args["usrname"] != usr] # Checks for bad username
      msg += ["","Bad Password!"][request.args["passwd"] != passwd] # Checks for bad password
    if not bool(msg): # authenticated successfully
      session["usr"] = request.args["usrname"]
      return redirect(url_for("welcome"))
  return render_template("login.html", msg = msg)

@app.route("/welcome")
def welcome():
  if "usr" in session:
    return render_template("welcome.html", usrname = session["usr"])
  return redirect("/")

# /logout ends the session and redirects to /
@app.route("/logout")
def logout():
  session.pop("usr", None)
  return redirect("/")

if __name__ == "__main__":
  app.run(debug = True)