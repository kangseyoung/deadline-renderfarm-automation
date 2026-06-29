import os

from pymongo import MongoClient

mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
database_name = os.getenv("MONGODB_DATABASE", "student_db")

client = MongoClient(mongo_uri)
db = client[database_name]
reservation_collection = db[os.getenv("MONGODB_RESERVATION_COLLECTION", "reservation")]
auth_collection = db[os.getenv("MONGODB_AUTH_COLLECTION", "auth_collection")]
