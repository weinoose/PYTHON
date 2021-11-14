import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

lr = LinearRegression()

# 1.1 - DATA IMPORT

dataa = pd.read_csv("linearregression.csv")

# 2.1 -Join to the "Independent DataFrame" and Resuming the whole process.
# ! TAHMİN ETMEYE YARAYAN DEĞER. BU BİLGİLER KULLANILARAK DEPENDENT VALUE TAHMİN EDİLECEK!
# ! USING THIS INFORMATION, DEPENDENT VALUE WILL BE ESTIMATED!

x = dataa[["Year"]].values

# 2.2 - Defining our the "Dependent DataFrame".
# ! DİĞER DEĞİŞKENLERE GÖRE TAHMİN EDİLEN DEĞER!
# ! THE VALUE WHICH IS GUESSED ACCORDING TO INDEPENDENT VALUE!

y = dataa[["Goals"]].values

# 3.1 - SPLITTING THE MODEL.

x_tr, x_ts, y_tr, y_ts = train_test_split(x,y,test_size=0.5,random_state=17)
df_y_ts = pd.DataFrame(data = y_ts, columns=["Goals"])

# 3.2 - FITTING.

lr.fit(x_tr,y_tr)

# 3.3 - PREDICTION.

tahmin = lr.predict(x_ts)
finaly = df_y_ts[["Goals"]].values.tolist()
t_goals = pd.DataFrame(data=finaly, columns=["T. Goals"])
p_goals = pd.DataFrame(data=tahmin, columns=["P. Goals"])
print(pd.concat([t_goals,p_goals], axis=1),"\n")

# 3.4 - METRICS.

print(f"\nR2 Score: {r2_score(np.array(y_ts), tahmin)}\n")

# 3.5 - PLOTTING.

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