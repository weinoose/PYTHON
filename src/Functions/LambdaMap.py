# Classic Way

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def square(num):
    for i in num:
        print(i**2)

square(numbers)

# The map method returns all the questions in the list.

def func(num):
    return num**2

result = list(map(func, numbers))
print(result)

# Same as map. The only difference is that it has created a temporary function in one line.

result = list(map(lambda num: num**2, numbers)) 
print(result)