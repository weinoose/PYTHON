# Multi-Conditional, One-Stage If-Elif-Else situation.

number = int(input("Insert a number: "))

if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} = 0")

# Single Condition, Multi-Stage If-Elif-Else state.

number = float(input(": "))

if (0 < number < 1) or (number<0):
    if 0 < number < 1:
        print(f"{number} is something decimal one. Cannot be assumed as even/odd.")
    else:
        print(f"{number} is negative. Cannot be assumed as even/odd.")
else:
    if number%2==0:
        print(f"{int(number)} is even.")
    elif number%2==1:
        print(f"{int(number)} is odd.")