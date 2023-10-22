from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://admin:admin1234@fastapi-mongodb-cluster.gks8qk3.mongodb.net/?retryWrites=true&w=majority"
)

db = client.todo_db

collection_name = db["todo_collection"]
