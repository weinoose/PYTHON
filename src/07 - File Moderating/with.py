# APPEND

with open("demo1.txt", "a", encoding="UTF-8") as file:
    file.write("\nJavaScript\nR\nRuby\nPHP\nAngular")

# READ

with open("demo1.txt", "r", encoding="UTF-8") as file:
    print(file.read())