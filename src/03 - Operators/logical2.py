liste = ["Beyaz", "Siyah", "Lacivert"]
string = "Python, şu an en popüler dillerden bir tanesidir ve öğrenmesi çok kolaydır."

result = "Yeşil" not in liste
result = "," in string
result = "j" not in string
result = ( "Siyah" in liste ) and ( "P" in string )

print(result)

#

x = 27
y = 5

result = (x > y**2) and (x > y + 10)
result = (x > (y**2)*2) or ( x > y + 20 )
print(result)