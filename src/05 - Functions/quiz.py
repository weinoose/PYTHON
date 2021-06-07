# Gönderilen kelimeyi belirtilen kez ekranda gösterilen fonksiyonu yazdırın. [TR]
# Print the sent word specified times the function shown on the screen.  [ENG]

"""x = int(input("Kelime kaç kere gösterilsin: "))

def func(word, count):
    print(word*count)
func("Python\n", x)"""

# Kendisine gönderilen sınırsız sayıdaki paremetreyi bir listeye çevir. [TR]
# Convert the unlimited number of parameters sent to it into a list.  [ENG]

"""def func(*params):
    liste = []
    for i in params:
        liste.append(i)
    print(liste)
func(1, 5, 12, "Python", True)"""

# Gönderilen 2 sayı arasındaki asal sayıları bulacağız. [TR]
# We will find the prime numbers between the 2 numbers sent.  [ENG]

"""def func(n1, n2):
    for i in range(n1, n2):
        if i > 1:
            for j in range(2, i):
                if (i%j==0):
                    break
            else:
                print(i)
func(0, 100)"""

# Kendisine gönderilen sayının tam bölenlerini bir liste şeklinde ekrana yazdır. [TR]
# Print the divisors of the number sent to him as a list on the screen.  [ENG]

"""def func(num):
    liste = []

    for i in range(2, num):
        if num%i==0:
            liste.append(i)
    return liste

print(func(120))"""