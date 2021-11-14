import sqlite3 as sql

database = sql.connect("tutorial.db")

cursor = database.cursor()

name = "Bradley Beal" 
ppg = 30.6
rpg = 2.8
apg = 4.7

insert = f"INSERT INTO basketball VALUES('{name}', '{ppg}', '{rpg}', '{apg}')"

cursor.execute(insert)

database.commit()

database.close()