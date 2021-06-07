# Kullanıcıdan aldığınız verilerle bir liste oluşturun. Listenin sonundaki elemanı silin. [TR]
# Create a list with the data you receive from the user. Delete the end of the list. [ENG] 

"""liste = []
x, y, z = input("Verileri yan yana ve aralarında boşluk olacak şekilde girin: ").split()
x, y, z = str(x), str(y), str(z)
liste.extend([x, y, z])
print(f"Orijinal liste: {liste}")
liste.pop(len(liste)-1)
print(f"Yeni liste: {liste}")"""

# Kullanıcıdan aldığınız float veriyi integer veriye çevirerek ekrana yazdırın [TR]
# Convert the float data you received from the user to integer data and print it on the screen [ENG] 
"""x = float(input("Ondalıklı bir sayı giriniz: "))
x = int(x)
print(x)"""

# Metot kullanarak String formatlama yapın. [TR]
# Format String using method. [ENG] 
"""x, y, z = input("Verileri yan yana ve aralarında boşluk olacak şekilde girin: ").split()
x, y, z = str(x), str(y), str(z)

string = "En sevdiğim araba markası {0}. Daha sonrasında şu markalar gelir : {1}, {2}.".format(x, y, z)
print(string)"""