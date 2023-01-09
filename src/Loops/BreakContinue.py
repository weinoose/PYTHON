# Continue Method

string = 'Python'

x = 0
while x < len(string):
    if string[x] == "y":
        x = x + 1
        continue
    else:
        print(string[x])
        x += 1

# Break Method

liste = ['Ship','Vehicle','Train','Plane']

x = 0
while True:
    if liste[x] == 'Vehicle':
        x += 1
        continue
    elif x == len(liste)-1:
        break
    else:
        print(liste[x])
        x += 1

# Selection Making

quest = int(input("Selection #1\nSelection #2\nYour choice: "))

while True:
    if quest == 1:
        print("Selection number 1 has choosen.")
        break
    elif quest == 2:
        print("Selection number 2 has choosen.")
        break
    else:
        print("Did the wrong choice.")
        break