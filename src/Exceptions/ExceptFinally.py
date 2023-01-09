def func(p):
    try:
        liste = ['Hamilton','Alonso','Vettel','Button','Rosberg']
        y = int(input("To access any element of the list, ask for an index number."))
        print(liste[y])
    except (IndexError):
        print("You exceeded the index limit of the list.")
        p += 1
    except (ValueError):
        print("Please enter an integer expression.")
        p += 1
    finally:
        print(f"Program terminated with {p} errors.")
        input(">>> Press ENTER to close the program.")

func(0)