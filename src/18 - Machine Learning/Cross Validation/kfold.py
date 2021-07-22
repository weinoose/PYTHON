import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

data = pd.read_csv("lda.csv")

x = data.iloc[:,0:13].values
y = data.iloc[:,13].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=17)

sc = StandardScaler()

x_train1 = sc.fit_transform(x_train)
x_test1 = sc.fit_transform(x_test)

# Regression

lr1 = LogisticRegression(random_state=17)
lr1.fit(x_train1,y_train)

pred1 = lr1.predict(x_test1)

# K-Fold Cross Validation
score = cross_val_score(estimator = lr1, X = x_train1, y = y_train, cv = 5)
print(score.mean())