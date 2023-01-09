def decorator(x):
    def returner():
        print("before function.")
        x()
        print("after function.")
    return returner

@decorator
def other():
    print(True)

other()