height = float(input("Insert your height as a meter: "))
weight = int(input("Insert your weight as a kilogram: "))
bmi = (weight/(height**2))

skinny = 19.5 > bmi
normal = 25.5 > bmi >= 19.5
overweight = 33.5 > bmi >= 25.5
obese = bmi >= 33.5

print(f"Skinny: {skinny}, BMI : {bmi}")
print(f"Normal: {normal}, BMI : {bmi}")
print(f"Overweight: {overweight}, BMI : {bmi}")
print(f"Obese: {obese}, BMI : {bmi}")