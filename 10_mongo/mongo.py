from pprint import pprint
from pymongo import MongoClient
from bson.json_util import loads


# function to handle data
def ingest(f):
    with open(f) as _f:
        return loads(_f.read())


# functions to for handling init
init_client = lambda uri: MongoClient(uri)
init_database = lambda client, database_name: client[database_name]


# functions to insert data
# ------------------------
# insert_data takes in a mongodb database created by the mongo connection
#   and inserts a bson object (after the file is read) into a collection called license.
insert_data = lambda database, f: database['license'].insert_many(ingest(f))


# util functions
def print_results(results):
  for result in results:
    pprint(result)