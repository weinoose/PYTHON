import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=100)

# E1 : Data Import

dataa = pd.DataFrame(pd.read_csv("decisiontree.csv"))

# E2 : Defining our dependent and independent data's.

x = dataa[["Weight","Age"]].values
y = dataa[["Height"]].values

# E3 : Fitting and Predicting
# Putting predictions right into datasets for visualization. 

dt.fit(x,y)
prediction = pd.DataFrame(data = dt.predict(x), columns=["P. Height"])
realone = pd.DataFrame(data=y,columns=["T. Height"])
resume = pd.concat([prediction, realone], axis=1)

print("Tabel of Predicted & Real Values\n",resume,"\n")
print("R2 Score:",r2_score(y,dt.predict(x)),"\n")

# E4 : Plotting

plt.ylabel("Predicted Height")
plt.xlabel("True Height")

plt.scatter(y.reshape(-1,1),dt.predict(x), color="red", s=15)
plt.show()