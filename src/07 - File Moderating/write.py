n = int(input("How many programming languages do you want to enter? At least 1 is accepted: "))
x = 1
c = input("Text: ")

file = open("demo1.txt", "w", encoding="UTF-8")
file.write(c)
file.close()

while x < n:
    p = input("Text: ")
    file = open("demo1.txt", "a", encoding="UTF-8")
    file.write(f"\n{p}")
    file.close()
    x += 1