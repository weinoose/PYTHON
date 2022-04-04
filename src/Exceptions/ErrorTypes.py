# ValueError: Error due to data type mismatch.
x = int(input())
print(x)

# TypeError: Operating with the wrong data type or performing operations that are not unique to the data type.
x = str(input())
print(x-15)

# ZeroDivisionError: Attempting to divide a mathematical expression by 'zero'.
print(15/0)

# IndexError: If the index number we want to reach exceeds the maximum index number of the list, this error is received.
liste = [1, 5, 8]
print(liste[3])

# NameError: This error is received if the names of embedded functions that come with Python are used incorrectly.
printf("Hello, World!")

# IndentationError: Occurs if TAB rule is not followed.
if True:
print("Statement is True.")

# SyntaxError: Error type that occurs when the spelling rules of the language are not followed.
print(len(*Merhaba*))