import mysql.connector as sql

try:
    connection = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "1234567Sql",
        database = "formula1"
    ) 
except:
    print("Database connection has disabled.")

connection.close()