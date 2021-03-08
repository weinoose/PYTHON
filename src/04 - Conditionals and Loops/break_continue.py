# CONTINUE

string = "Python"

x = 0
while x < len(string):
    if string[x] == "y":
        x = x + 1
        continue
    else:
        print(string[x])
        x += 1

# BREAK

liste = ["Köpek", "Kedi", "Kaplumbağa", "Kuş", "At"]

x = 0
while True:
    if liste[x] == "Kaplumbağa":
        x += 1
        continue
    elif x == len(liste)-1:
        break
    else:
        print(liste[x])
        x += 1

# SELECTIONS

quest = int(input("Aşağıdakilerden birini seç\n1 - 5 Milyon dolar nakit para\n2 - Işınlanma yeteneği\n3 - Dünyadaki tüm dilleri bilmek.\nSeçiminiz: "))

while True:
    if quest == 1:
        print("Para hesabınıza yatırıldı")
        break
    elif quest == 2:
        print("Yeteneğiniz aktifleştirildi.")
        break
    elif quest == 3:
        print("Tüm diller hafızanıza yüklendi.")
        break
    else:
        print("Hatalı seçim yaptınız. Şansınızı kaybettiniz.")
        break