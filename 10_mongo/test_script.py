# Jun Tao Lei
# SoftDev pd9
# K10 -- Opensource Licenses with MongoDB
# 2020-03-03

# Dataset: Opensource Licenses
# Desc: A collection of all opensource software licenses found in opensource.org.
# Rawdata: https://api.opensource.org/licenses/

from mongo import (
  init_client,
  init_database,
  insert_data,
  print_results
)
from licenses import (
  find_by_name,
  find_by_identifier,
  find_by_keyword,
  find_by_keywords,
  find_by_filter
)


# init test database
mongo_client = init_client('mongodb://localhost:27017/')
database = init_database(mongo_client, 'opensource')


# insert licenses from json file
insert_data(database, 'opensoftware-licenses.json')


# test queries...
print_results(
  find_by_name(
    database,
    'GNU General Public License, Version 3.0'
  )
)
print_results(
  find_by_identifier(
    database,
    'MIT'
  )
)
print_results(
  find_by_keyword(
    database,
    'copyleft'
  )
)
print_results(
  find_by_keyword(
    database,
    ['osi-approved', 'popular']
  )
)
print_results(
  find_by_filter(
    database,
    'obsolete'
  )
)