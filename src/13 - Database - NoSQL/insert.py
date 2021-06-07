import pymongo

def MongoInsert():
    # Connection
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    database = connection["Products"]
    myCollection = database["Gamebook"]

    # One Row Insert
    inserted = {
        "title" : "Gamebook FK0002-U",
        "CPU" : 8,
        "GPU" : 2,
        "RAM" : 4,
        "Monitor" : 60
    }

    result1 = myCollection.insert_one(inserted)

    # Many Row Insert

    inserted = [{
        "title" : "Gamebook FK0002-U",
        "CPU" : 8,
        "GPU" : 2,
        "RAM" : 4,
        "Monitor" : 60
    },
    {
        "title" : "Gamebook Future"
    }
    ]

    result2 = myCollection.insert_many(inserted)

    return result1, result2

print(MongoInsert())