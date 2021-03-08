import mysql.connector as sql

def getItem(request):
    database = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "1234567Sql",
        database = "formula1"
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

getItem("SELECT * FROM drivers")
getItem("SELECT * FROM drivers Order by titles")
getItem("SELECT * FROM drivers Where titles >= 1")