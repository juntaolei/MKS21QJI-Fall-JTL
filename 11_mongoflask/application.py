from flask import (
  g,
  Flask,
  render_template,
  request
)
from mongo import (
  init_client,
  init_database,
  insert_data
)


app = Flask(__name__)


with app.app_context():
  g.client = init_client('mongodb://localhost:27017/')

  g.licenses = init_database(g.client, 'licenses')
  g.meteorites = init_database(g.client, 'meteorites')

  insert_data(g.licenses['opensource'], 'opensoftware-licenses.json')
  insert_data(g.meteorites['earth_landings'], 'meteorites.json')


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/query')
def query():
  query_type = request.args['selectQueryType']
  raw_query = request.args['searchQuery']
  return 'done'


if __name__ == '__main__':
  app.run(debug=True)
