import mysql.connector as sql

try:
    browser = sql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Cool%%27",
        database = "formula1"
    )
    browser.close()
except:
    print("Database connection has disabled.")