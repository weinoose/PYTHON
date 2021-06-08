import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

lr = LinearRegression()
model = Sequential()

# 1.1 - Data Import
dataa = pd.read_csv("linearregression.csv")

# 2.1 -Join to the "Independent DataFrame" and Resuming the whole process.
# ! TAHMİN ETMEYE YARAYAN DEĞER. BU BİLGİLER KULLANILARAK DEPENDENT VALUE TAHMİN EDİLECEK.
# ! USING THIS INFORMATION, DEPENDENT VALUE WILL BE ESTIMATED.
x = pd.DataFrame(dataa[["Year"]])

# 2.2 - Defining our the "Dependent DataFrame".
# ! DİĞER DEĞİŞKENLERE GÖRE TAHMİN EDİLEN DEĞER.
# ! THE VALUE WHICH IS GUESSED ACCORDING TO INDEPENDENT VALUE.
y = pd.DataFrame(dataa[["Goals"]])

# 3.1 - Splitting our model between train and test.
x_tr, x_ts, y_tr, y_ts = train_test_split(x,y,test_size=0.5,random_state=17)

# 3.2 - Fitting the Data.
lr.fit(x_tr,y_tr)

# 3.3 - Guess Algorithm.
tahmin = lr.predict(x_ts)
finaly = y_ts["Goals"].values.tolist()
t_goals = pd.DataFrame(data=finaly, columns=["T. Goals"])
p_goals = pd.DataFrame(data=tahmin, columns=["P. Goals"])
print(pd.concat([t_goals,p_goals], axis=1),"\n")

# 3.4 - Plotting Struct.
x_tr = x_tr.sort_index()
y_tr = y_tr.sort_index()

plt.xlim(2001.5,2021.5)
plt.ylim(0,10)
plt.plot(x_tr,y_tr)
plt.plot(x_ts,tahmin)
plt.show()

# 3.5 - R2 Score Calculation.
print(f"\nR2 Score: {r2_score(np.array(y_ts), tahmin)}\n")

# 3.6 - Building our Neural Network.

model.add(Dense(2,activation="relu"))
model.add(Dense(2,activation="relu"))

model.add(Dense(1))

model.compile(optimizer="rmsprop", loss="mse")

model.fit(x_tr, y_tr, epochs=300)

# 3.7 - Gathering Teorical Results.

loss = model.history.history["loss"]

sbn.lineplot(x=range(len(loss)), y=loss)
trainLoss = model.evaluate(x_tr, y_tr, verbose=0)
testLoss = model.evaluate(x_ts, y_ts, verbose=0)

print("\nTrain Loss:",trainLoss)
print("\nTest Loss:",testLoss,"\n")