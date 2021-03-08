import sqlite3 as sql

database = sql.connect("tutorial.db")

cursor = database.cursor()

cursor.execute("SELECT * FROM basketball") # Gathers the all Columns
# cursor.execute("SELECT * FROM basketball WHERE name = 'Bradley Beal'") # Gathers the specific column
# cursor.execute("SELECT * FROM basketball where ppg > 35.5") # Gathering the filtered column.
# cursor.execute("SELECT * FROM basketball Order by ppg") # Ordering the specific column.

data = cursor.fetchall()

print(data)