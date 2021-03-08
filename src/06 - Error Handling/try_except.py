try:    
    x = int(input("Enter an Integer greater than 2:"))
    print(x-2)
except (ValueError):
    print("Please enter an Integer expression .")
    y = input(">>> Press ENTER to close the program. <<<")

#

try:
    x = int(input("Enter denominator:"))
    print(25/x)
except (ZeroDivisionError):
    print("You cannot divide the number by 0.")
    input(">>> Press ENTER to close the program. <<<")
except (ValueError):
    print("Do not enter a String or Bool expression.")
    input(">>> Press ENTER to close the program. <<<")