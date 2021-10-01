# [Just TR descriptions available]

file = open("demo1.txt", "r", encoding="UTF-8")

# result = file.read() # Dosyanın içeriğini okumamızı sağlar.
# result = file.readline() # Dosyanın ilk satırını okumamızı sağlar.
result = file.readlines() # Dosyanın istediğimiz satırını okumamızı sağlar.
file.close()

print(result[2])