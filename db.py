from pymongo import MongoClient
import os

# 🔹 Get MongoDB URI
MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    raise Exception("❌ MONGO_URI not set in environment variables")

# 🔹 Safe MongoDB connection
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # test connection
except Exception as e:
    raise Exception(f"❌ MongoDB connection failed: {str(e)}")

# 🔹 Database & Collection
db = client["iot_db"]
collection = db["sensor_data"]


# 🔹 Insert data
def insert_data(data):
    try:
        collection.insert_one(data)
    except Exception as e:
        print("Insert Error:", e)


# 🔹 Fetch data
def get_all_data():
    try:
        return list(collection.find({}, {"_id": 0}))
    except Exception as e:
        print("Fetch Error:", e)
        return []
