import json

# dict to json convert.

example1 = {
    "Name" : "Emir Yarkın",
    "Surname" : "Yaman"
}

result = json.dumps(example1)

with open("pythoncourse.json", "a", encoding="UTF-8") as file:
    file.write(result)

# json to dict convert.

file = open("pythoncourse.json", "r")

result = json.loads(file.read())
print(result)

file.close()