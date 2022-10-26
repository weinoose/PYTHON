import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

lr = LinearRegression()

# E1 : Data Import

dataa = pd.read_csv("linearregression.csv")

# E2 : Defining our dependent and independent data's.

x = dataa[["Year"]].values
y = dataa[["Goals"]].values

# E2.1 : Splitting the model into train and test.

x_tr, x_ts, y_tr, y_ts = train_test_split(x,y,test_size=0.5,random_state=17)
df_y_ts = pd.DataFrame(data = y_ts, columns=["Goals"])

# E3 : Fitting and Predicting
# Putting predictions right into datasets for visualization. 

lr.fit(x_tr,y_tr)
tahmin = lr.predict(x_ts)
finaly = df_y_ts[["Goals"]].values.tolist()
t_goals = pd.DataFrame(data=finaly, columns=["T. Goals"])
p_goals = pd.DataFrame(data=tahmin, columns=["P. Goals"])
print(pd.concat([t_goals,p_goals], axis=1),"\n")

# E3.1 : Metrics and Scores

print(f"\nR2 Score: {r2_score(np.array(y_ts), tahmin)}\n")

# E4 : Plotting

d1 = pd.DataFrame(data = x_tr, columns = ["X_TR"])
d2 = pd.DataFrame(data = y_tr, columns = ["Y_TR"])
dd = pd.concat([d1,d2],axis=1).sort_values("X_TR", ascending=True) 
x = dd[["X_TR"]].values
y = dd[["Y_TR"]].values

plt.xlim(2001.5,2021.5)
plt.ylim(0,10)
plt.plot(x,y)
plt.plot(x_ts,tahmin)
plt.show()