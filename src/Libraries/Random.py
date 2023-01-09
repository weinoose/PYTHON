from random import random, randrange, shuffle, uniform, randint, choice

# print(dir(random)) - Kütüphanenin içine bakmamızı sağlar.

# Number Affiliated
# 0-1 arasında float.
result = random()

# float.
result = uniform(0, 100)

# integer, right boundary does not included.
result = randrange(86, 87) 

# integer, right boundary does included.
result = randint(86, 87)

# List Affiliated
liste = [True, False, 17, 7, "Hello!", "Hi!"]

# random selection.
result = choice(liste)

# shuffles the list.
shuffle(liste)
print(liste)