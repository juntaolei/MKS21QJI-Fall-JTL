# Jun Tao Lei & Connor Oh
# SoftDev1 pd9
# K12 -- Jinja Forming
# 2019-09-25

from flask import Flask, render_template, request

# Instantiate Flask
app = Flask(__name__)                                       

@app.route("/")                                
def foo():
  return render_template("foo.html")

@app.route("/auth")
def auth():
  print(app)
  print(request)
  print(request.args)
  print(request.args["username"])
  print("HEADERSSSSS")
  print(request.headers)
  name = request.args["username"]
  return render_template("auth.html", user = name)

app.run(debug = True)
