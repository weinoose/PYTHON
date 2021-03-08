import pymongo
from pymongo import results

def MongoGet():
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    database = connection["Products"]
    myCollection = database["Gamebook"]

    # Get All
    result = list(myCollection.find({}))
    for i in result:
        print(i)
    
    # Filter Method

    result = myCollection.find({     
        "title" : {
            "$in" : ["Gamebook FK0002-U"]
        }
    })

    result2 = myCollection.find({
        "CPU" : {
            "$eq" : 8
        }
    })

    for i in result:
        print(i)

    for j in result2:
        print(j)

    # Order By
    print()
    result2 = list(myCollection.find().sort("CPU", -1)) # -1 Descending | 1 Ascending
    print(result2)

MongoGet()