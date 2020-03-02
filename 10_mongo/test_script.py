from mongo import (
  init_client,
  init_database,
  insert_data
)
from licenses import (
  find_by_name,
  find_by_identifier,
  find_by_keyword
)


# init test database
mongo_client = init_client('mongodb://localhost:27017/')
database = init_database(mongo_client, 'opensource')


# insert licenses from json file
insert_data(database, 'opensoftware-licenses.json')


# test queries...
# TBD