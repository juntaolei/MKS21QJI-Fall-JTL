import ingest
import pprint
import controller

new_client = controller.init_client('mongodb://localhost:27017/')
db = controller.init_db(new_client, 'restaurants')

# res = controller.insert_restaurants_by_borough(db, 'primer-dataset.json')

cursor = controller.get_all_by_borough(db, db['Bronx'])
