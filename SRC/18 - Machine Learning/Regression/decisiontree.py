import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=100)

# 1 - DATA IMPORT.

dataa = pd.DataFrame(pd.read_csv("decisiontree.csv"))

# 2.1 - Defining the "Independent DataFrame".
# ! TAHMİN ETMEYE YARAYAN DEĞER. BU BİLGİLER KULLANILARAK DEPENDENT VALUE TAHMİN EDİLECEK!
# ! USING THIS INFORMATION, DEPENDENT VALUE WILL BE ESTIMATED!

x = dataa[["Weight","Age"]].values

# 2.2 - Defining the "Dependent DataFrame".
# ! DİĞER DEĞİŞKENLERE GÖRE TAHMİN EDİLEN DEĞER!
# ! THE VALUE WHICH IS GUESSED ACCORDING TO INDEPENDENT VALUE!

y = dataa[["Height"]].values

# 4 - FITTING.

dt.fit(x,y)

# 5 - PREDICTION.

prediction = pd.DataFrame(data = dt.predict(x), columns=["P. Height"])
realone = pd.DataFrame(data=y,columns=["T. Height"])
resume = pd.concat([prediction, realone], axis=1)

print("Tabel of Predicted & Real Values\n",resume,"\n")
print("R2 Score:",r2_score(y,dt.predict(x)),"\n")

# 6 - PLOTTING.

plt.ylabel("Predicted Height")
plt.xlabel("True Height")

plt.scatter(y.reshape(-1,1),dt.predict(x), color="red", s=15)
plt.show()