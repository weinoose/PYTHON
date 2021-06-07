import mysql.connector as sql

def updateItem(name, titles):
    database = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "1234567Sql",
        database = "formula1"
    ) 
    cursor = database.cursor()
    request = "UPDATE drivers SET titles = %s Where name = %s"
    values = (titles, name)
    cursor.execute(request, values)

    try:
        database.commit()
        print(f"{cursor.rowcount} adet kayıt güncellendi.")
    except (sql.Error) as err:
        print(f"Hata : {err}")
    finally:
        database.close()
        print("Database kapandı...")

updateItem("Carlos Sainz Jr.", 0)