import ingest
import pymongo

# functions to for handling init
init_client = lambda uri: pymongo.MongoClient(uri)
init_db = lambda client, database_name: client[database_name]

# insertion functions
insert_restaurants_by_borough = lambda db, f: list(map(lambda r: db[r['borough']].insert(r), ingest.ingest(f)))

# query functions
get_all_by_borough = lambda borough, collection: collection.find({'borough': borough})
