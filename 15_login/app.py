from flask import Flask, session, redirect, url_for, render_template, request
from os import urandom

app = Flask(__name__)

app.secret_key = urandom(32)

# FAKE USRNAME
usr = "admin"
# FAKE PASSWORD
passwd = "admin"

@app.route("/")
def root():
  if "usr" in session:
    return redirect(url_for("welcome"))
  return redirect(url_for("login"))

@app.route("/login", methods = ["GET"])
def login():
  if request.args and request.args["usrname"] == usr:
    session["usr"] = request.args["usrname"]
    return redirect(url_for("welcome")) 
  else:
    return render_template("login.html")

@app.route("/welcome")
def welcome():
  return render_template("welcome.html", usrname = session["usr"])

@app.route("/logout")
def logout():
  session.pop("usr", None)
  return redirect("/")

if __name__ == "__main__":
  app.run(debug = True)