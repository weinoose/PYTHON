# Section 1

x = 10
y = 8

result = x > y
result = x < y
result = x == y
result = x != y
result = x >= y
result = x <= y

print(result)

# Section 2

p, v = input().split()
p, v = int(p), int(v)
result = p >= v
print(f"{p} is equal-greater than {v}: {result}")

# Section 3

liste = ['White','Black','Gray']
string = "White, black and gray defined as colors."

result = "Yeşil" not in liste
result = "," in string
result = "j" not in string
result = ("Siyah" in liste) and ("P" in string)

print(result)