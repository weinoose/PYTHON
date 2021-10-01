def func(p):
    try:
        liste = ["Muz", "Elma", "Şeftali", "Armut", "Kayısı", "Kavun"]
        y = int(input("To access any element of the list, ask for an Index number. : "))
        print(liste[y])
    except (IndexError):
        print("You exceeded the index limit of the list.")
        p += 1
    except (ValueError):
        print("Please enter an Integer expression.")
        p += 1
    finally:
        print(f"Program terminated with {p} errors.")
        input(">>> Press ENTER to close the program. <<<")

func(0)