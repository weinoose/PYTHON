x = 10
y = 8

result = x > y
result = x < y
result = x == y
result = x != y
result = x >= y
result = x <= y

print(result)

#

p, v = input().split()
p, v = int(p), int(v)
result = p >= v
print(f"{p} is equal-greater than {v}: {result}")