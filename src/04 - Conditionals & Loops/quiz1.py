# Vücut kütle indexine göre bir bireye fitness mesajı yazdırın. [TR]
# Print a fitness message to an individual based on their body mass index. [ENG] 

height = float(input("Insert your height as meter: "))
weight = int(input("Insert your weight a kilogram: "))
bmi = (weight)/(height**2)

if 19.5 > bmi > 0:
    print("Zayıf. | BMI : {0}".format(bmi))
elif 25.5 > bmi >= 19.5:
    print("Normal. | BMI : {0}".format(bmi))
elif 31.5 > bmi >= 25.5:
    print("Fazla Kilolu. | BMI : {0}".format(bmi))
elif 100 >= bmi >= 31.5:
    print("Obez. | BMI : {0}".format(bmi))
else:
    print("Yanlış veri girdiniz. Tekrar deneyin")

# Ehliyet kontrol ifadesi yazdırın, 18 yaşından büyük ve sınavdan 75+ lazım. [TR]
# Print a driving license check statement, you need over 18 years old and 75+ from the exam. [ENG] 

age = int(input("Insert your age: "))

if age >= 18:
    print("Sınava girebilirsiniz.")
    exam = int(input("Sınav puanınızı giriniz: "))
    if exam >= 75:
        print("Ehliyet alabilirsiniz.")
    else:
        print("Sınavda başarısız oldunuz. Tekrar deneyiniz.")
else:
    print("Sınava girmeniz için 18 yaşında olmanız gerekmektedir.")