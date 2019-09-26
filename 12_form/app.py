#Nahi Khan, Connor Oh, Winston Peng [Team Beaker]

#SoftDev1 pd9

#K10 -- Jinja Tuning

#2019 - 09 - 23

from flask import Flask, render_template, request

app = Flask(__name__)                                       #instantiate Flask

@app.route("/")                                #the route we will be using to access our table
def foo():
    print(app)
    return render_template(
        'foo.html'
    )

@app.route("/auth")
def auth():
    print(request)
    print(request.args)
    return "ok"

app.run(debug = True)
