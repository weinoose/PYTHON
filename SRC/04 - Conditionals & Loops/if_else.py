besinler = ["Mantı", "Pazı Kavurması", "Lahana Sarması", "Su", "Bonfile"]
n = str(input("Bir besin gir: "))

if n in besinler:
    print(f"{n} bir besindir.")
else:
    print(f"{n} bir besin değildir.")