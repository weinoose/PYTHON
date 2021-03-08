import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017")
database = connection["Products"]
myCollection = database["Gamebook"]

print(myCollection)