# You can use enumarate in for to achieve index numbers of elements.

liste = ["Real Madrid", "Internazionale dé Milan", "PSV Eindovhen"]

for i in enumerate(liste):
    print(i)
    print(type(i))

# Range is the artificial limiter for the for loop.

total = 0
for i in range(0, 101):
    total = i + total
print(total)

# Section 1

count = int(input("How many inputs would you make: "))

for i in range(count):
    input("Enter your input: ")

# Section 2

num = int(input("Until which number?: "))

for i in range(num):
    if i%2==1:
        print(i)