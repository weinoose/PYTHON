import re
import pandas as pd 
from nltk.corpus import stopwords
from sklearn.metrics import accuracy_score
from nltk.stem.porter import PorterStemmer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

data = pd.DataFrame(pd.read_csv("sentiment.tsv", sep='\t'))
x, comments = 0, []

ps = PorterStemmer()
cv = CountVectorizer(max_features = 2500)
gnb = GaussianNB()

while x < 1000:
    comment = re.sub("[^a-zA-Z]"," ",data["Review"][x]).lower().split()
    comment = [ps.stem(word) for word in comment if not word in set(stopwords.words("english"))]
    comment = ' '.join(comment)
    comments.append(comment)
    x += 1

x = cv.fit_transform(comments).toarray()
y = data.iloc[:,1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.9, random_state = 31)

gnb.fit(x_train, y_train)
prediction = gnb.predict(x_test)

cm = confusion_matrix(y_test, prediction)
ratio = (cm[0,0] + cm[1,1])/(cm[0,1] + cm[1,0] + cm[0,0] + cm[1,1])

print(f"\nConfusion Matrix Success Ratio is: {ratio}\n")

metric_s = accuracy_score(y_test,prediction)

print(f"\nSklearn Metrics Success Ratio is: {metric_s}\n")

df1 = pd.DataFrame(data=comments, columns=["Comments"])
df2 = pd.DataFrame(data=data["Liked"])
df3 = pd.DataFrame(data=prediction, columns=["P. Liked"])
finaldf = pd.concat([df2,df3,df1],axis=1).head(900)

print(f"\nComprasion DF between M.L. and Real Values\n\n{finaldf}\n")