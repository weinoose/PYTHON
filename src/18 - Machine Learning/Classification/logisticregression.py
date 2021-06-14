import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

sc = StandardScaler()
logr = LogisticRegression(random_state=31)

# DATA IMPORT.

veri = pd.DataFrame(pd.read_csv("logisticregression.csv"))

# DEFINING X & Y.

x = veri[["Height","Weight","Age"]].values
y = veri[["Gender"]].values

# DIVIDING BETWEEN TEST AND TRAIN.

x_tr,x_ts,y_tr,y_ts = train_test_split(x, y, test_size=0.5, random_state=31)

# FIT & TRANSFORM.

x_train = sc.fit_transform(x_tr)
x_test = sc.transform(x_ts)

# PREDICTION.

logr.fit(x_train,y_tr)
prediction = logr.predict(x_test)

# FINAL PART.

real = veri[["Gender"]].head(11)
pred = pd.DataFrame(prediction, columns=["P. Gender"])
cm = confusion_matrix(y_ts, prediction)
true = cm[1][1] + cm[0][0]
false = cm[1][0] + cm[0][1]
result = pd.concat([pred, real], axis=1)
print(result,"\n")
print(f"True: {true} | False {false} | Success Ratio %{(true/(true+false))*100}\n")
tp = (cm[0][0] / ( cm[0][0] + cm[1][0] ))*100
fp = (cm[0][1] / ( cm[0][1] + cm[1][1] ))*100
print(f"True Positive Rate : %{tp} | False Positive Rate : %{fp}\n")
