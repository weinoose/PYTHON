import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

# 1 - Including the Data.
dataa = pd.read_csv("multipleregression.csv")

# IF THERE IS A CATEGORICAL VALUE IN YOUR DATA FRAME. 
# ! If not, pass the 2nd part.
# 1.1 - Defining our Functions.
le = preprocessing.LabelEncoder()
ohe = preprocessing.OneHotEncoder()
lr = LinearRegression()
scaler = MinMaxScaler()

# 1.2 - Categorical to Numerical Convert 
# ! Defining Column's which has categorical values.
# ! Column's index number is x. 
# ! For that reason interval selection is between x and x + 1 ( 1 is not included )
countries = dataa.iloc[:,0:1].values
genders = dataa.iloc[:,4:5].values
# ! Column's index number is x.
countries[:,0] = le.fit_transform(dataa.iloc[:,0])
genders[:,0] = le.fit_transform(dataa.iloc[:,4])

# 1.3 - Numerical to Array & Column Structer.
# ! Check here, The order of the column names is determined here. 
# ! Look for 31th and 33th row.
countries = ohe.fit_transform(countries).toarray()
genders = ohe.fit_transform(genders).toarray()

# 1.4 - Preparing Splitted Data Frames.
result1 = pd.DataFrame(data=countries, index=range(22), columns=["GBR","TUR","USA"])
result2 = pd.DataFrame(dataa[["Height","Weight","Age"]])
result3 = pd.DataFrame(data=genders[:,:1], index=range(22), columns=["Gender"])

# 2.1 - Defining our the "Independent DataFrame".
# ! TAHMİN ETMEYE YARAYAN DEĞER. BU BİLGİLER KULLANILARAK DEPENDENT VALUE TAHMİN EDİLECEK.
# ! USING THIS INFORMATION, DEPENDENT VALUE WILL BE ESTIMATED.
dependent = pd.concat([result1, result2], axis=1)

# 2.2 - Defining our the "Dependent DataFrame".
# ! DİĞER DEĞİŞKENLERE GÖRE TAHMİN EDİLEN DEĞER.
# ! THE VALUE WHICH IS GUESSED ACCORDING TO INDEPENDENT VALUE.
independent = result3

# 2.3 - Pandas Columns to DataFrame Values.
x = dependent.values
y = independent.values

# 3.1 - Fitting & Preparing the Prediction Value as pd.df
lr.fit(x,y)
tahmin = lr.predict(x)
prediction = pd.DataFrame(tahmin, columns=["P. Gender"])
resume = pd.concat([prediction, dependent], axis=1)
resume["T. Gender"] = result3["Gender"]
print("Tabel of Predicted & Real Values\n",resume,"\n")
print("R2 Score:",r2_score(y,tahmin),"\n")

# 4 - Plotting Struct.
x = resume["T. Gender"].values.tolist()
y = resume["P. Gender"].values.tolist()

plt.scatter(x,y)
plt.title("Gender Prediction\nReferanced from Linear Plot.")
plt.show()