import pymongo
import pymongo

def MongoGet():
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    database = connection["Technology"]
    myCollection = database["Gamebook"]

    # Get All
    result = list(myCollection.find({}))
    for i in result:
        print(i)
    
    # Filter Method

    result = myCollection.find({     
        "title" : {
            "$in" : ["Asus TUF Gaming"]
        }
    })

    result2 = myCollection.find({
        "RAM" : {
            "$eq" : 16
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