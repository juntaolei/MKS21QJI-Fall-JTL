import bson
import ingest
import pymongo

# utils
pprint = lambda data: type(data)

# functions to for handling init
init_client = lambda uri: pymongo.MongoClient(uri)

init_db = lambda client, database_name: client[database_name]

# insertion functions
insert_restaurants_by_borough = lambda db, f: list(
        map(
            lambda r: db[r['borough']].insert_one(dict(r)),
            ingest.ingest(f)
        )
    )

# query functions
get_all_by_borough = lambda borough, collection: list(
        map(lambda i: dict(i), collection.find())
    )

get_all_by_zipcode = lambda zipcode, db: filter(
        None,
        list(
            map(
                lambda c: list(
                    map(lambda i: dict(i), db[c].find({"address.zipcode": zipcode}))
                ),
                ['Bronx', 'Brooklyn', 'Manhattan', 'Staten Island', 'Missing', 'Queens']
            )
        )
    )

get_all_by_zipcode_and_grade = lambda zipcode, grade, db: filter(
        None,
        list(
            map(
                lambda c: list(
                    map(lambda i: dict(i), db[c].find({"address.zipcode": zipcode, "grades.0.grade": grade}))
                ),
                ['Bronx', 'Brooklyn', 'Manhattan', 'Staten Island', 'Missing', 'Queens']
            )
        )
    )

get_all_by_zipcode_and_score = lambda zipcode, score, db: filter(
        None,
        list(
            map(
                lambda c: list(
                    map(lambda i: dict(i), db[c].find({"address.zipcode": zipcode, "grades.0.score": {"$lt": int(score)}}))
                ),
                ['Bronx', 'Brooklyn', 'Manhattan', 'Staten Islan', 'Missing', 'Queens']
            )
        )
    )
