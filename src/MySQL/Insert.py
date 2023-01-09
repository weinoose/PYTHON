import mysql.connector as sql

def insertItem(title, wins):
    connection = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Cool%%27",
        database = "formula1"
    ) 

    cursor = connection.cursor()

    request = "INSERT INTO drivers(title, wins) VALUES(%s, %s)"
    values = (title, wins)

    cursor.execute(request, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} adet kayıt eklendi.")
    except (sql.Error) as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
        print("Database kapandı.")

insertItem("Carlos Sainz Jr.", 0)
insertItem("Charles Leclerc", 2)
insertItem("Sebastian Vettel", 53)
insertItem("Lance Stroll", 0)
insertItem("Fernando Alonso", 32)
insertItem("Esteban Ocon", 1)
insertItem("Daniel Ricciardo", 8)
insertItem("Lando Norris", 0)
insertItem("Lewis Hamilton", 100)
insertItem("George Russell", 0)
insertItem("Max Verstappen", 17)
insertItem("Sergio Perez", 2)
insertItem("Valtteri Bottas", 9)
insertItem("Robert Kubica", 1)
insertItem("Nikita Mazepin", 0)
insertItem("Mick Schumacher", 0)
insertItem("Pierre Gasly", 1)
insertItem("Yuki Tsunoda", 0)
insertItem("Nicholas Latifi", 0)
insertItem("Alexander Albon", 0)