import sqlite3 as sql

database = sql.connect("tutorial.db")

cursor = database.cursor()

# Gathers the all Columns.
cursor.execute("SELECT * FROM basketball")
# Gathers the specific column.
cursor.execute("SELECT * FROM basketball WHERE name = 'Bradley Beal'") 
# Gathering the filtered column.
cursor.execute("SELECT * FROM basketball where ppg > 35.5")
# Ordering the specific column.
cursor.execute("SELECT * FROM basketball Order by ppg")

data = cursor.fetchall()

print(data)