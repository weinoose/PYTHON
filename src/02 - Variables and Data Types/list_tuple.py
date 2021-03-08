# LİSTE SYNTAX

y = "Torro Rosso"
liste = ["McLaren", "Racing Point", "Ferrari", "Mercedes", "Renault", y]

# Achieving the list elements, # ! Indexing !
# print(liste[2])

# LIST METHODS

# liste.clear() # Resetting the list.
liste.append("BMW") # Adds an element to the end of the list. 
liste.insert(6, "Red Bull Racing") # Adds an element to specified position of the list. 
liste.pop(5) # It is given the index number of any element in the list. 
liste.remove("Racing Point") # Gives itself any element in the list. 
liste.reverse() # Inverts the list. 
liste.sort() # Sorts in ascending order. 
index_number = liste.index("McLaren")

print(f"McLaren's index number is : {index_number}")
print(liste)

# TUPLE LIST'S

tuple1 = ("Elma", "Muz", "Karpuz", "Kavun", "Şeftali")
index2 = tuple1.index("Karpuz")
print(index2)

# CONVERTING BETWEEN TUPLE AND A LIST

liste = tuple(liste)
print(liste)

tuple1 = list(tuple1)
print(tuple1)