# Jun Tao Lei (Of TeamKubica With Calvin Chu)
# SoftDev1 pd9
# K#10 -- Template Displaying Random Occupations / Dictionary + Flask + Jinja2 / Display a table of occupations and a random occupation.
# 2019-09-20

from flask import Flask, render_template, redirect, url_for

# User Created
from utl.urlify import urlify
from utl.randoccupation import getoccupations, randoccupation

# Instantiate a Flask instance
app = Flask(__name__)

# Create a Python dictionary of the occupations in ./static/occupations.csv and added corresponding url.
urlify_jobs = urlify(getoccupations("./data/occupations.csv"), "https://www.indeed.com/jobs?q=")

# Redirect / to /occupyflaskst to avoid having to type /occupyflaskst in browser
@app.route("/")
def index():
  return redirect(url_for("occupyflaskst"))

# Return a render of the template and given the correct context.
@app.route("/occupyflaskst")
def occupyflaskst(jobs = urlify_jobs):
  randjob = randoccupation(jobs)
  return render_template("occupyflaskst.html", randoccupation = randjob, jobs = jobs)

if __name__ == "__main__":
  app.run(debug = True)