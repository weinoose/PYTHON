# [Just TR descriptions available.]

from random import random, randrange, shuffle, uniform, randint, choice

# print(dir(random)) - Kütüphanenin içine bakmamızı sağlar.

# SAYILARLA ALAKALI OLAN KISIM

result = random() # 0-1 arasında float bir sayı döndürür.

result = uniform(0, 100) # Verilen 2 parametre arasında rastgele bir float sayı döndürür.

result = randrange(86, 87) # Verilen 2 parametre arasında rastgele bir integer sayı döndürür. 
# İlk parametre dahilken ikinci parametre dahil değildir.

result = randint(86, 87) # Verilen 2 parametre arasında rastgele bir integer sayı döndürür. 
# İki parametre de dahildir.

# LİSTELERLE ALAKALI OLAN KISIM

liste = [True, False, 17, 7, "Hello!", "Hi!"]

result = choice(liste) # Parametre olarak verilen listeden rastgele bir eleman seçer.

shuffle(liste) # İçine verilen parametre bir liste ise, listenin elemanlarını karışık olarak sıralar.

print(liste)