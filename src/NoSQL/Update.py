import pymongo

def MongoUpdate():
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    database = connection["technology"]
    myCollection = database["Gamebook"]

    query = {"title" : "Asus TUF Gaming"}

    updated = (
        {"$set" : {
            "Monitor" : 144
        }}
    )

    result = myCollection.update_one(query, updated)
    print(result)

MongoUpdate()