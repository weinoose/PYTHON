question = int(input("1 - DOMESTIC FLIGHT\n2 - INTERNATIONAL FLIGHT\nMake your choice: "))

def flight(limit):
    liste = []
    p = int(input("Insert the luggage count: "))
    for i in range(p):
        i = int(input("Insert the luggage weight: "))
        liste.append(i)
    total = sum(liste)
    
    if total <= limit:
        print("You are ready to flight.")
    else:
        print("Your total baggage weight is over the limit.")


if question == 1:
    flight(35)
elif question == 2:
    flight(45)
else:
    print("Made the wrong choice.")