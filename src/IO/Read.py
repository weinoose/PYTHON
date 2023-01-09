file = open("demo1.txt", "r", encoding="UTF-8")

# Result returns whole content of the file.
result = file.read()
# Result returns first row of the file to operate. 
result = file.readline()
# Result returns all rows of the file into a list to operate. 
result = file.readlines()

file.close()
print(result[2])