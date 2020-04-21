import os
import csv
import json
from flask import Flask, g, jsonify, send_file
from app.scrape import scrape

app = Flask(__name__, static_folder='static')
app.config.from_mapping(
    ROOT_DIR=os.path.dirname(os.path.abspath(__file__))
)

scrape(f'{app.static_folder}')


@app.route('/')
def index():
    return send_file(os.path.join(os.path.join(app.config['ROOT_DIR'], 'public'), 'index.html'))


@app.route('/data')
def data():
    array = []
    with open(f'{app.static_folder}/covid19.csv', 'r') as f:
        field_names = ('U.S. state or territory', 'Cases',
                       'Deaths', 'Recoveries', 'Hospitalizations')
        reader = csv.DictReader(f, field_names)
        next(reader, None)
        for row in reader:
            array.append(json.loads(json.dumps(row)))
    return jsonify(array)
