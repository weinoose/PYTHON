def decorator(x):
    def returner():
        print("Fonksiyondan önce.")
        x()
        print("Fonksiyondan sonra.")
    return returner

@decorator
def other():
    print(True)

other()