from pymongo import MongoClient
import os

MONGO_URI = os.environ.get("MONGO_URI")

client = None
collection = None

try:
    if MONGO_URI:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client["iot_db"]
        collection = db["sensor_data"]
except Exception as e:
    print("MongoDB Error:", e)


def insert_data(data):
    if collection:
        collection.insert_one(data)


def get_all_data():
    if collection:
        return list(collection.find({}, {"_id": 0}))
    return []
