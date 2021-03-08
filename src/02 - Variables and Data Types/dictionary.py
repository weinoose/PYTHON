person = {
    "Name" : "Emir Yarkın",
    "Age" : 18,
    "Title" : "Student"
}

result = person
result = person["Name"] # Spesifik bir Key kullanarak Value kısmına ulaşma.
person["Name"] = "Elon Musk" # Güncelleme işlemi.
del person["Age"] # İstediğimiz key kısmını silebiliyoruz.
result = person.values() # Tüm değerleri almamızı sağlar.
person.clear()

print(person)

# # #

person = {
    1000 : {
        "Name" : "Jeff Bezos",
        "Age" : 57,
        "Title" : "Amazon.com Founder"
    },
    1001 : {
        "Name" : "Elon Musk",
        "Age" : 49,
        "Title" : "SpaceX Founder"
    }
}

result = person.values()
result = person[1001]["Name"]
print(result)