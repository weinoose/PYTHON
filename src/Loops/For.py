# Section 1

liste = ['Python','Go','Java','C']

for i in liste:
    print(f'\n{i}')
    print(f"{i} liste elemanıdır.")
    print(f'{len(i)}\n')

# Section 2

string = 'Python is one of the easy languages with a lot powers.' 

for i in string:
    print(i)

# Section 3

dictionary = {
    "Name" : "Christian",
    "Surname" : "Bale",
    "Movie" : "The Prestige"
}

for i in dictionary.values():
    print(i)

# Section 4

liste = [0,1,2,3,4,5,6,7,8,9]

for i in liste:
    if i%2==0:
        print(i)