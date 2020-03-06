from flask import (
  g,
  Flask
)
from mongo import (
  init_client,
  init_database,
  insert_data
)


app = Flask(__name__)


with app.app_context():
  g['client'] = init_client('mongodb://localhost:27017/')

  g['licenses'] = init_database(g['client'], 'licenses')
  g['meteorites'] = init_database(g['client'], 'meteorites')

  insert_data(g['licenses']['opensource'], 'opensoftware-licenses.json')
  insert_data(g['meteorites']['earth_landings'], 'meteorites.json')


@app.route('/')
def index():
  return 'Hello, world!'


if __name__ == '__main__':
