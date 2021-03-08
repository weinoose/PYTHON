# [Just TR Descriptions available.]

text = "Python Öğrenmesi hem çok kolay hem de çok zevklidir! Python öğreniyorum"

result = text.upper() # Tüm karakterleri büyük harfe çevirir.
result = text.lower() # Tüm karakterleri küçük harfe çevirir.
result = text.capitalize() 
# Sadece ilk kelimenin baş harfini büyük yapar. Cümle içindeki diğer kelimelerden herhangi biri büyük harfle başlıyorsa onu küçültür.
result = text.title() # Capitalize ama her kelimeye etki eder. Büyüğü küçük yapmaz.
result = text.strip() # String ifadenin başındaki boşlukları yok eder.
result = text.split() # String ifadeyi kelimelerine ayırır.
result = text.split("!") # String ifadeyi içine verdiğimiz parametreye göre ayırır.
result = text.replace("zevklidir!", "eğlencelidir!")
result = text.replace(" ", "") # String ifadedeki tüm boşlukları kaldırır.
result = text.startswith("p") # Textin ne ile başladığıyla ilgili soru sorulur.
result = text.endswith("m") # Textin ne ile bittiği ile ilgili soru sorulur.

print(result)