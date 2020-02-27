import ingest
import controller

new_client = controller.init_client('mongodb://localhost:27017/')
db = controller.init_db(new_client, 'restaurants')

# result = controller.insert_restaurants_by_borough(db, 'primer-dataset.json')

restaurants_by_borough = controller.get_all_by_borough(db, db['Bronx'])
restaurants_by_zip = controller.get_all_by_zipcode('10005', db)
restaurants_by_zip_and_grade = controller.get_all_by_zipcode_and_grade('10005', 'A', db)
restaurants_by_zip_and_score = controller.get_all_by_zipcode_and_score('10005', '5', db)

print("Restaurants in Bronx:")
for restaurant in restaurants_by_borough:
    print(restaurant)

print("\nRestaurants within 10005")
for restaurant in restaurants_by_zip:
    print(restaurant)

print("\nGrade A Restaurants within 10005")
for restaurant in restaurants_by_zip_and_grade:
    print(restaurant)

print("\nRestaurants within 10005 Below a Score of 5")
for restaurant in restaurants_by_zip_and_score:
    print(restaurant)
