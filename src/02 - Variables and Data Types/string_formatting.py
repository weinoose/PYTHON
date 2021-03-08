name = str(input("Insert your name: "))
age = int(input("Insert your age: "))
title = str(input("Insert your job title: "))

# RADITIONAL WAY, Classic string formatting

text = "Benim adım {}, {} yaşındayım ve {} mesleğini sürdürmekteyim.".format(name, age, title)
print(text)

# MODERN WAY, f'String usage.

text = f"Benim adım {name}, {age} yaşındayım ve {title} mesleğini sürdürmekteyim."
print(text)