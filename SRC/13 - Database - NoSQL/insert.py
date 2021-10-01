import pymongo

def MongoInsert():
    # Connection
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    database = connection["Technology"]
    myCollection = database["Gamebook"]

    # One Row Insert
    inserted = {
        "title" : "Monster Tulpar T7",
        "CPU" : "Intel i7-11800H",
        "GPU" : "nVIDIA RTX 3060",
        "RAM" : 16,
        "Monitor" : 144
    }

    result1 = myCollection.insert_one(inserted)

    # Many Row Insert

    inserted = [{
        "title" : "Lenovo Legion 5",
        "CPU" : "AMD Ryzen 7 5800H",
        "GPU" : "nVIDIA RTX 3060",
        "RAM" : 16,
        "Monitor" : 165
    },
    {
        "title" : "Asus TUF Gaming",
        "CPU" : "Intel i7-11350H",
        "GPU" : "nVIDIA RTX 3050Ti",
        "RAM" : 32,
        "Monitor" : 60
    }
    ]

    result2 = myCollection.insert_many(inserted)

    return result1, result2

print(MongoInsert())