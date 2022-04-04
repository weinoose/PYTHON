import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

# E1 : Data Import

dataa = pd.read_csv("multipleregression.csv")

# Defining our outer functions for label encoding.

le = preprocessing.LabelEncoder()
ohe = preprocessing.OneHotEncoder()
lr = LinearRegression()
scaler = MinMaxScaler()

# Encoder : Categoric to Numeric Convert.
# x = column's index number.
# for that reason interval selection is between x and x + 1, also 1 is not included.

countries = dataa.iloc[:,0:1].values
genders = dataa.iloc[:,4:5].values
countries[:,0] = le.fit_transform(dataa.iloc[:,0])
genders[:,0] = le.fit_transform(dataa.iloc[:,4])
countries = ohe.fit_transform(countries).toarray()
genders = ohe.fit_transform(genders).toarray()

# Merge operations for recreating the dataframe.

result1 = pd.DataFrame(data=countries, index=range(22), columns=["GBR","TUR","USA"])
result2 = pd.DataFrame(dataa[["Height","Weight","Age"]])
result3 = pd.DataFrame(data=genders[:,:1], index=range(22), columns=["Gender"])

# E2 : Defining our dependent and independent data's.

dependent = pd.concat([result1, result2], axis=1)
independent = result3
x = dependent.values
y = independent.values

# E3 : Fitting and Predicting
# Putting predictions right into datasets for visualization. 

lr.fit(x,y)
tahmin = lr.predict(x)
prediction = pd.DataFrame(tahmin, columns=["P. Gender"])
resume = pd.concat([prediction, dependent], axis=1)
resume["T. Gender"] = result3["Gender"]
print("Tabel of Predicted & Real Values\n",resume,"\n")
print("R2 Score:",r2_score(y,tahmin),"\n")

# E4 : Plotting

x = resume["T. Gender"].values.tolist()
y = resume["P. Gender"].values.tolist()

plt.scatter(x,y)
plt.title("Gender Prediction\nReferanced from Linear Plot.")
plt.show()