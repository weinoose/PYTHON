# SET'S

a = {1,3,5,7,9,11}
b = {1,3,6,9,12}

result = a | b # Birleşim Kümesi | Combination Set 
result = a & b # Kesişim Kümesi | Intersection Set 
result = a - b # Fark Kümesi | Difference Set

print(result)

# REMOVING THE DUPLICATES IN LISTS

liste = [1, 2, 2, 3, 3, 3]
liste = set(liste)
liste = list(liste)
print(liste)