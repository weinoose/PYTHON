import mysql.connector as sql

def insertItem(name, position, age, goal):
    connection = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "1234567Sql",
        database = "soccer"
    ) 

    cursor = connection.cursor()

    request = "INSERT INTO fcbayern(name, position, age, goal) VALUES(%s, %s, %s, %s)"
    values = (name, position, age, goal)

    cursor.execute(request, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} adet kayıt eklendi.")
    except (sql.Error) as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
        print("Database kapandı.")

def getItem(request):
    database = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "1234567Sql",
        database = "soccer"
    ) 

    cursor = database.cursor()
    cursor.execute(request)

    try:
        result = cursor.fetchall()
        for i in result:
            print(i)
    except sql.Error as err:
        print(f"Hata : {err}")
    finally:
        database.close()
        print("Database bağlantısı kapandı...")

liste = [
    ("Manuel Neuer","Goalkeeper", 34, 0),
    ("David Alaba","Defender", 28, 2),
    ("Jerome Boateng","Defender", 32, 2),
    ("Benjamin Pavard","Wing-Back", 24, 0),
    ("Alphonso Davies","Wing-Back", 20, 1),
    ("Joshua Kimmich","Right Midfielder", 25, 4),
    ("Leon Goretzka","Left Midfielder", 25, 4),
    ("Thomas Mueller","Attack Midfielder", 31, 18),
    ("Serge Gnabry","Wing-Forward", 25, 6),
    ("Leroy Sane","Wing-Forward", 24, 7),
    ("Robert Lewandowski","Striker", 32, 28)
]

for i in liste:
    insertItem(i[0],i[1],i[2],i[3])

getItem("SELECT * FROM fcbayern")
getItem("SELECT * FROM fcbayern Order by age")
getItem("SELECT * FROM fcbayern Where goal >= 5 Order by goal")