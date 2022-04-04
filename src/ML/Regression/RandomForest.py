import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators = 100, random_state = 100)

# E1 : Data Import

dataa = pd.read_csv("randomforest.csv")

# E2 : Defining our dependent and independent data's.

independent = pd.DataFrame(dataa[["cp","trtbps","chol","fbs","restecg","thalachh","exng","oldpeak","slp","caa","output"]])
dependent = pd.DataFrame(dataa[["age","sex"]])

x = independent.values
y = dependent.values

# E3 : Fitting and Predicting
# Putting predictions right into datasets for visualization. 

rf.fit(x,y)
prediction = pd.DataFrame(rf.predict(x), columns=["p. age","p. sex"])
resume = pd.concat([prediction, dependent], axis=1)
print("Tabel of Predicted & Real Values\n",resume,"\n")
print("R2 Score:",r2_score(y,rf.predict(x)),"\n")

# E4 : Plotting

x = dataa["age"].tolist()
plt.ylabel("Predicted Age")
plt.xlabel("True Age")
plt.scatter(x,resume["p. age"].values.tolist(), color="red", s=17)
plt.show()