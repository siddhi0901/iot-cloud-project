from pymongo import MongoClient
import os

MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI not set in environment variables")

client = MongoClient(MONGO_URI)

db = client["iot_db"]
collection = db["sensor_data"]


# 🔹 Insert data
def insert_data(data):
    collection.insert_one(data)


# 🔹 Fetch data
def get_all_data():
    return list(collection.find({}, {"_id": 0}))