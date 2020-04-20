import os
from flask import Flask
from scrape import scrape

app = Flask(__name__, static_folder='static')
app.config.from_mapping(
    ABSPATH=os.path.dirname(os.path.abspath(__file__))
)

scrape(f'{app.static_folder}')


def index():
    return "Hello, world!"
