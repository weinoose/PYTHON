# Global Variable
x = 5

def func():
    # Local Variable
    y = 2
    print(x)
    print(y)

func()

x = 3

def func():
    print(x)

# Calling Local x.
func()
# Calling Global x.
print(x)

x = 10

def func():
    global x
    x = 15

func()
print(x)