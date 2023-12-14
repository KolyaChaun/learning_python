import json
import certifi
import pymongo
import eigth_lesson_mongo_config

url = "mongodb+srv://{user}:{password}@project1.q3aston.mongodb.net/?retryWrites=true&w=majority".format(
    user=eigth_lesson_mongo_config.USER_MONGO,
    password=eigth_lesson_mongo_config.PASSWORD_MONGO,
)

client = pymongo.MongoClient(url, tlsCAFile=certifi.where())

db = client["Text"]
quotes_coll = db["Quotes"]

# RECORDING QUOTES IN A DATABASE
with open("eight_lesson_data.json", "r", encoding="utf-8") as file:
    quotes_data = json.load(file)
quotes_coll.insert_many(quotes_data["quotes"])

# GET QUOTES Einstein
query = {"author": "Albert Einstein"}
result = quotes_coll.find(query)

for quotes_albert in result:
    print(quotes_albert["quote"])

# GET QUOTES WITH SUCCESS
query = {"quote": {"$regex": "success"}}
result = quotes_coll.find(query)

for quotes_albert in result:
    print(quotes_albert["quote"])

# ADD A NEW FAVORITE FIELD
filter_data = {"author": "Mark Twain"}
new_data = {"$set": {"favorite": True}}
processed = quotes_coll.update_many(filter_data,new_data)

# REMOVE QUOTES FROM THE AUTOR VAN GOGH
query_van_gogh = {"author": "Vincent Van Gogh"}
deleted = quotes_coll.delete_many(query_van_gogh)
print(deleted)

# DELETE ALL DATA
query = {}
deleted = quotes_coll.delete_many(query)
