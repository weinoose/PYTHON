import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

sc = StandardScaler()
rfc = RandomForestClassifier(n_estimators=17, criterion="entropy")

# DATA IMPORT.

veri = pd.DataFrame(pd.read_csv("randomforest.csv"))

# DEFINING X & Y.

x = veri[["age","cp","trtbps","chol","fbs","restecg","thalachh","exng","oldpeak","slp","caa","thall","output"]].values
y = veri[["sex"]].values

# DIVIDING BETWEEN TEST AND TRAIN.

x_tr,x_ts,y_tr,y_ts = train_test_split(x, y, test_size=0.5, random_state=31)

# FIT & TRANSFORM.

x_train = sc.fit_transform(x_tr)
x_test = sc.transform(x_ts)

# PREDICTION.

rfc.fit(x_train,y_tr)
prediction = rfc.predict(x_test)

# FINAL PART.

real = veri[["sex"]].head(15)
pred = pd.DataFrame(prediction, columns=["P. Sex"])
cm = confusion_matrix(y_ts, prediction)
true = cm[1][1] + cm[0][0]
false = cm[1][0] + cm[0][1]
result = pd.concat([pred, real], axis=1)
print(result,"\n")
print(f"True: {true} | False {false} | Success Ratio %{(true/(true+false))*100}\n")
tp = (cm[0][0] / ( cm[0][0] + cm[1][0] ))*100
fp = (cm[0][1] / ( cm[0][1] + cm[1][1] ))*100
print(f"True Positive Rate : %{tp} | False Positive Rate : %{fp}\n")