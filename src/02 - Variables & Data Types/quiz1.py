# Kullanıcıdan aldığınız bilgilerle bir Dictionary oluşturun ve bu bilgileri ekrana yazdırın. [TR]
# Create a Dictionary with the information you get from the user and print this information on the screen. [ENG] 

"""x = str(input("Insert your name here: "))
y = int(input("Insert your age here: "))
z = str(input("Insert your favourite colour here: "))

person = {}

person["Name"] = x
person["Age"] = y
person["Favourite Colour"] = z

print(person)"""


# Kullanıcıdan aldığınız 3 sayıyı küçükten büyüğe doğru sıralayın. [TR]
# Order the 3 numbers you get from the user in ascending order. [ENG] 
"""liste = []
n1, n2, n3 = input("Karşılaştırılmasını istediğiniz 3 sayıyı arada bir boşluk olacak şekilde yan yana yazınız: ").split()
n1, n2, n3 = int(n1), int(n2), int(n3)
liste.extend([n1, n2, n3])
x = max(liste)
y = min(liste)
liste.remove(max(liste))
liste.remove(min(liste))
print(f"{x} > {liste[0]} > {y}")"""



# Kullanıcıdan aldığınız bilgilerle ona bir karşılama mesajı yazdırın. [TR]
# Print a welcome message with the information you received from the user. [ENG] 
"""x = str(input("Insert your name here: "))
y = int(input("Insert your age here: "))
z = str(input("Insert your favourite colour here: "))

print(f"My name is {x}. I'm {y} years old. My favourite color is {z}.")"""


# Duplicate içeren bir liste alalım ve duplicatelerin silinmiş halini yazdıralım. [TR]
# Let's take a list with duplicates and print the deleted version of the duplicates. [ENG] 
"""liste = [0, 5, 5, 6, 6, 6, 7, 8, 45, 13, "e", "w", "w"]
liste = set(liste)
liste = list(liste)
print(liste)"""