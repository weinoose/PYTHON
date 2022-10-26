import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

data = pd.read_csv("lda.csv")

x = data.iloc[:,0:13].values
y = data.iloc[:,13].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=17)

sc = StandardScaler()

x_train1 = sc.fit_transform(x_train)
x_test1 = sc.fit_transform(x_test)

# LDA

lda = LDA(n_components = 2)
x_train2 = lda.fit_transform(x_train,y_train)
x_test2 = lda.transform(x_test)

# Regression

lr1 = LogisticRegression(random_state=17)
lr1.fit(x_train1,y_train)

lr2 = LogisticRegression(random_state=17)
lr2.fit(x_train2,y_train)

pred1 = lr1.predict(x_test1)
pred2 = lr2.predict(x_test2)

# Result

print("\nReal vs Non-LDA Analysis!")
print(confusion_matrix(y_test,pred1),"\n")

print("Real vs With-LDA Analysis!")
print(confusion_matrix(y_test,pred2),"\n")

print("Non-LDA Analysis vs With-LDA Analysis!")
print(confusion_matrix(pred1,pred2),"\n")