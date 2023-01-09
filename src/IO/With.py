# 'with' keyword using for minimizing the memory leaks.

# Append

with open("demo1.txt", "a", encoding="UTF-8") as file:
    file.write("\nJavaScript\nR\nRuby\nPHP\nAngular")

# Read

with open("demo1.txt", "r", encoding="UTF-8") as file:
    print(file.read())