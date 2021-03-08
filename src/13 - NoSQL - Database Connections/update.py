import pymongo

def MongoUpdate():
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    database = connection["Products"]
    myCollection = database["Gamebook"]

    query = {"title" : "Gamebook FK0002-U"}

    updated = (
        {"$set" : {
            "Monitor" : 144
        }}
    )

    result = myCollection.update_one(query, updated)
    print(result)

MongoUpdate()