from os import urandom
from flask import Flask, render_template

from urllib.request import urlopen
from json import loads, dumps

app = Flask(__name__)

app.secret_key = urandom(32)


@app.route("/")
def index():
    print("REPLACE YOUR_API_KEY WITH A VALID API KEY")
    # API key should not be pushed to GitHub
    try:
        req = urlopen(
            "https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY"
        )
        res = req.read()
        data = loads(res)
        return render_template(
            "base.html",
            title=data["title"],
            pic=data["url"],
            date=data["date"],
            explanation=data["explanation"]
        )
    except:
        return render_template(
            "base.html",
            title="REPLACE YOUR_API_KEY WITH A VALID API KEY."
        )


if __name__ == "__main__":
    app.run(debug=True)
