# Jun Tao Lei
# SoftDev1 pd9
# K#09
# 2019-09-20

from flask import Flask, render_template

app = Flask(__name__)

col = [0, 1, 1, 2, 3, 5, 8]

@app.route("/my_foist_template")
def foist():
  return render_template("my_foist_template.html", d = col)

if __name__ == "__main__":
  app.run(debug = True)