# [Just TR descriptions available.]

import os
import platform

result = os.name # İşletim sisteminizin adını print eder.
result = platform.system() # İşletim sisteminizin adını print eder.
result = platform.release() # İşletim sisteminizin sürümünü print eder.
result = os.system("pip install pandas") # CMD kod satırı işlevi görür.
result = os.getcwd() # Dosya yolu verir.
result = os.mkdir("Example") # Kodu yazdığınız dizinde bir klasör açar.
result = os.rename("practice.py","mymodule.py") # 2 Parametre alır. İlk parametre orijinal dosyanın ismidir. Dosya ismi değiştirir.
result = os.listdir()
os.remove("pythoncourse.json")