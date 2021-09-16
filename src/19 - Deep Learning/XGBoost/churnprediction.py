import keras
import numpy as np
import pandas as pd
from keras.layers import Dense
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn import preprocessing
from keras.models import Sequential
from sklearn.metrics import confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Importer : Data Include.

data = pd.read_csv('churnprediction.csv')

x = data.iloc[:,3:13].values
y = data.iloc[:,13].values

# Encoder : Categoric to Numeric Convert.

le = preprocessing.LabelEncoder()
x[:,1] = le.fit_transform(x[:,1])

le2 = preprocessing.LabelEncoder()
x[:,2] = le2.fit_transform(x[:,2])

ohe = ColumnTransformer([("ohe", OneHotEncoder(dtype=float),[1])],remainder="passthrough")
x = ohe.fit_transform(x)
x = x[:,1:]

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

sc=StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

# Neural : Neural Network Design.

model = Sequential()

model.add(Dense(6, kernel_initializer = 'uniform', activation = 'relu' , input_dim = 11))
model.add(Dense(6, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(1, kernel_initializer = 'uniform', activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss =  'binary_crossentropy' , metrics = ['accuracy'] )
model.fit(x_train, y_train, epochs=50)

y_pred = model.predict(x_test)
y_pred = (y_pred > 0.5)

# Result : Final Review.

cm = confusion_matrix(y_test,y_pred)
print(f"\nTensorflow Result: \n{cm}")

# XGBoost Part.

xgb = XGBClassifier()
xgb.fit(x_train,y_train)

y_xgb = xgb.predict(x_test)

cmx = confusion_matrix(y_test,y_xgb)
print(f"\nXGBoost Result: \n{cmx}")