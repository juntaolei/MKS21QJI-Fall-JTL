# Jun Tao Lei
# SoftDev pd9
# Flask app worked on in class
# 2019-09-19

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder="static")

class Duck:
  def __init__(self, name, traits):
    self.name = name
    self.traits = traits

@app.route("/")
def index():
  return app.send_static_file("index.html")

@app.route("/", methods=["POST"])
def duck():
  name = request.form["name"]
  traits = request.form["traits"].split(" ")
  duck = Duck(name, traits)
  if len(name) > 0 and len(traits) > 0:
    return render_template("duck.html", aduck = duck)
  else:
    return redirect("/")

if __name__ == "__main__":
  app.debug = True
  app.run()  