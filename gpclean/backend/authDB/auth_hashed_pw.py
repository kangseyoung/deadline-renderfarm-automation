import hashlib
import os

from pymongo import MongoClient


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017"))
db = client[os.getenv("MONGODB_DATABASE", "student_db")]
collection = db[os.getenv("MONGODB_AUTH_COLLECTION", "auth_collection")]


def add_students_to_mongo(auth_dict):
    """Insert public-safe sample users or locally supplied private users."""

    for student_id, plain_password in auth_dict.items():
        if check_registered_user(student_id):
            print(f"Already registered: {student_id}")
            continue

        hashed_pw = hash_password(plain_password)
        collection.insert_one({
            "student_id": student_id,
            "password_hash": hashed_pw
        })
        print(f"Registered: {student_id}")


def make_sample_dictionary():
    return {
        "<student-id-1>": "<sample-password-1>",
        "<student-id-2>": "<sample-password-2>",
    }


def check_registered_user(student_id):
    return collection.find_one({"student_id": student_id}) is not None


if __name__ == "__main__":
    add_students_to_mongo(make_sample_dictionary())
