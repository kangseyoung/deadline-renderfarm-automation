# db.py
from pymongo import MongoClient

# 전역으로 한 번만 연결
client = MongoClient("mongodb://localhost:27017")
db = client["student_db"]
reservation_collection = db["reservation"]
auth_collection = db["auth_collection"]