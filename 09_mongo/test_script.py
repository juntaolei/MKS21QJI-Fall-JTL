import ingest
import controller


# init new client and create a new database
new_client = controller.init_client('mongodb://localhost:27017/')

db = controller.init_db(new_client, 'restaurants')


# insert the data in the json file into the database
result = controller.insert_restaurants_by_borough(db, 'primer-dataset.json')


# get all restaurants from Bronx
restaurants_by_borough = controller.get_all_by_borough(db, 'Bronx')


# get all restaurants in 10005
restaurants_by_zip = controller.get_all_by_zipcode(db, '10005')


# get all restaurants in 10005 with grade A
restaurants_by_zip_and_grade = controller.get_all_by_zipcode_and_grade(db, '10005', 'A')


# get all restaurants in 10005 with score below 5
restaurants_by_zip_and_score = controller.get_all_by_zipcode_and_score(db, '10005', '5')


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
