"""x = 5 # Global Variable

def func():
    y = 2 # Local Variable
    print(x)
    print(y)

func()"""

#

"""x = 3

def func():
    print(x)

func() # Calling Local x.
print(x) # Calling Global x."""

#

x = 10

def func():
    global x
    x = 15

func()
print(x)