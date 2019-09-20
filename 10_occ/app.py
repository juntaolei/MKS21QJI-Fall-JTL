# Jun Tao Lei
# SoftDev1 pd9
# K#10
# 2019-09-20

from csv import DictReader as d
from random import choices as c
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

def getoccupations(file):
  dictionary = {}
  for row in d(open(file)):
    dictionary[row["Job Class"]] = float(row["Percentage"])
  return dictionary

def randoccupation(dictionary):
  tdict = dictionary.copy()
  tdict.pop("Total")
  keys, values = zip(*tdict.items())
  return c(keys, values)[0]

jobs = getoccupations("occupations.csv")

@app.route("/")
def index():
  return redirect(url_for("occupyflaskst"))

@app.route("/occupyflaskst")
def occupyflaskst(randoccupation = randoccupation(jobs), jobs = jobs):
  return render_template("occupyflaskst.html", randoccupation = randoccupation, jobs = jobs)

@app.route("/occupyflaskst", methods = ["POST"])
def updateoccupy():
  return occupyflaskst(randoccupation(jobs))

if __name__ == "__main__":
  app.debug = True
  app.run()