import numpy as np
a = np.array([[1,9,5],[7,3,11]])

# SORT

print("Main Array:")
print(a)
print("\n")

print("After the sort() function:")
print(np.sort(a))
print("\n")

# ORDER

dt = np.dtype([("name", "S50"), ("age", int)])
a = np.array([("Beckham", 44),("Cristiano",36),("Xavi",41),("Iniesta",36)], dtype = dt)

print("Main Array:")
print(a)
print("\n")

print("Order by Age:")
print(np.sort(a, order="age"))
print("\n")

print("Order by Name:")
print(np.sort(a, order="name"))
print("\n")