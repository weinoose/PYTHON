# Various mathematical operations are performed with the result of math operators.

x = int(input("Inster the 1st Numuber: "))
y = int(input("Insert the 2nd Number: "))

# Addition

result = x + y
print(result)

# Multiplication

result = x * y
print(result)

# Division

result = x / y
print(result)

# Subtraction

result = x - y
print(result)

# Full Division

result = x // y
print(result)

# Power

result = x**y
print(result)

# Transaction Priority

result = ((x**y)/x)-y+x
print(result)

# Mixed Transactions

x = 27
y = 5

result = (x > y**2) and (x > y + 10)
result = (x > (y**2)*2) or ( x > y + 20 )
print(result)