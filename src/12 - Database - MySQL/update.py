import mysql.connector as sql

def updateItem(title, wins):
    database = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Cool%%27",
        database = "formula1"
    ) 
    cursor = database.cursor()
    request = "UPDATE drivers SET wins = %s Where title = %s"
    values = (wins, title)
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