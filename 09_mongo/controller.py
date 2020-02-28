from ingest import ingest
from itertools import chain
from pymongo import MongoClient


# functions to for handling init
init_client = lambda uri = '': MongoClient(uri)

init_db = lambda client, database_name: client[database_name]


# insertion functions
insert_restaurants_by_borough = lambda db, f: list(
        map(
            lambda r: db[r['borough']].insert_one(r),
            ingest(f)
        )
    )


# query functions
get_all_by_borough = lambda db, borough: list(
        db[borough].find()
    )

get_all_by_zipcode = lambda db, zipcode: list( 
        chain.from_iterable(
            map(
                lambda c: list(
                    db[c].find({"address.zipcode": zipcode})
                ),
                db.collection_names()
            )
        )
    )

get_all_by_zipcode_and_grade = lambda db, zipcode, grade: list(
        chain.from_iterable(
            map(
                lambda c: list(
                    db[c].find({"address.zipcode": zipcode, "grades.0.grade": grade})
                ),
                db.collection_names()
            )
        )
    )

get_all_by_zipcode_and_score = lambda db, zipcode, score: list(
        chain.from_iterable(
            map(
                lambda c: list(
                    db[c].find({"address.zipcode": zipcode, "grades.0.score": {"$lt": int(score)}})
                ),
                db.collection_names()
            )
        )
    )
