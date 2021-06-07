import mysql.connector as sql

def insertItem(name, titles):
    connection = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "1234567Sql",
        database = "formula1"
    ) 

    cursor = connection.cursor()

    request = "INSERT INTO drivers(name, titles) VALUES(%s, %s)"
    values = (name, titles)

    cursor.execute(request, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} adet kayıt eklendi.")
    except (sql.Error) as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
        print("Database kapandı.")

insertItem("Carlos Sainz Jr.", 1)