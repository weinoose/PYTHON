import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=17)

# 1 - Including the Data
dataa = pd.read_csv("decisiontree.csv")

# 2.1 - Defining the "Independent DataFrame".
# ! TAHMİN ETMEYE YARAYAN DEĞER. BU BİLGİLER KULLANILARAK DEPENDENT VALUE TAHMİN EDİLECEK
# ! USING THIS INFORMATION, DEPENDENT VALUE WILL BE ESTIMATED
x = pd.DataFrame(dataa[["Weight","Age"]])

# 2.2 - Defining the "Dependent DataFrame".
# ! DİĞER DEĞİŞKENLERE GÖRE TAHMİN EDİLEN DEĞER
# ! THE VALUE WHICH IS GUESSED ACCORDING TO INDEPENDENT VALUE
y = pd.DataFrame(dataa[["Height"]])

# 4 - Fitting the Data.
dt.fit(x,y)

# 5 - Result of Prediction Algorithm
tahmin = dt.predict(x)
prediction = pd.DataFrame(tahmin, columns=["P. Height"])
resume = pd.concat([prediction, y], axis=1)
print("Tabel of Predicted & Real Values\n",resume,"\n")
print("R2 Score:",r2_score(y,tahmin),"\n")

# 6 - Plotting the Result
x = dataa["Height"].tolist()
plt.ylabel("Predicted Height")
plt.xlabel("True Height")
plt.scatter(x,tahmin, color="red", s=15)
plt.show()