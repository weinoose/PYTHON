import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

veri = pd.DataFrame(pd.read_csv("kmeans.csv"))

x = veri[["Age","Volume","Salary"]].values

km = KMeans(n_clusters = 3, init = "k-means++", random_state = 17)
clusters = km.fit_predict(x)

plt.title("KMeans Clustering")
plt.scatter(x[clusters==0,0], x[clusters==0,1], s=100, c="red")
plt.scatter(x[clusters==1,0], x[clusters==1,1], s=100, c="blue")
plt.scatter(x[clusters==2,0], x[clusters==2,1], s=100, c="green")
plt.show()