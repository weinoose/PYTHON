numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def square(num):
    for i in num:
        print(i**2) # Classic Way

square(numbers)

#
# Map metodu listedeki tüm elemanları sırasıyla döndürür. [TR]
# The map method returns all the questions in the list. [ENG]

def func(num):
    return num**2

result = list(map(func, numbers))
print(result)

#
# Map ile aynı. Tek farkı tek satırda geçici bir fonksiyon oluşturmuş olması. [TR]
# Same as map. The only difference is that it has created a temporary function in one line. [ENG]

result = list(map(lambda num: num**2, numbers)) 
print(result)