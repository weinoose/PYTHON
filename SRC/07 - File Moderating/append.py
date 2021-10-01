d = input("Text: ")

file = open("demo1.txt", "a", encoding="UTF-8")
file.write(f"\n{d}")
file.close()