from itertools import chain
from pymongo import MongoClient
from bson.json_util import loads


def ingest(f):
    with open(f) as _f:
        return loads(_f.read())


# functions to for handling init
init_client = lambda uri: MongoClient(uri)
init_database = lambda client, database_name: client[database_name]
