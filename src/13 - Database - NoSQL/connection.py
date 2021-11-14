import pymongo

connection = pymongo.MongoClient("mongodb://localhost:27017")
database = connection["Technology"]
myCollection = database["Gamebook"]

print(myCollection)