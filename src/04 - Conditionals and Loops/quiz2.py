# [Just TR Descriptions available.]

liste = []
for i in range(101):
    liste.append(i)

# Listedeki sayılardan 3'ün katı olanlarını bul?

for i in liste:
    if (i%3==0) and (i != 0):
        print(i)


# Listedeki sayıların toplamını döngü yazarak bul?

total = 0

for i in liste:
    total = total + i
print(total)

#

print(sum(liste))


# Listedeki tek sayıların kareleri?

liste2 = []

for i in liste:
    if i%2==1:
        liste2.append(i**2)
print(sum(liste2))


# 1'den 100'e kadar olan tek sayıların küpü ile çift sayıların karesini topla

p = 1
total = 0
while True:
    if p == 101:
        break
    elif p%2==0:
        total += p**2
        p += 1
    elif p%2==1:
        total += p**3
        p += 1

print(total)

# Kullanıcıdan karışık bir şekilde alacağımız sayıları ekrana büyükten küçüğe şeklinde sıralayalım

liste = []

for i in range(5):
    i = int(input("Sayıyı gir: "))
    liste.append(i)

liste.sort()
liste.reverse()
print(liste)