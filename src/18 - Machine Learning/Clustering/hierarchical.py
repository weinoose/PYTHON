import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch 
from sklearn.cluster import AgglomerativeClustering

veri = pd.DataFrame(pd.read_csv("hierarchical.csv"))

x = veri[["Age","Volume","Salary"]].values

agg = AgglomerativeClustering(n_clusters = 3, affinity="euclidean", linkage="ward")
clusters = agg.fit_predict(x)

plt.title("Agglomerative Hierarchical Clustering")
plt.scatter(x[clusters==0,0], x[clusters==0,1], s=75, c="red")
plt.scatter(x[clusters==1,0], x[clusters==1,1], s=75, c="blue")
plt.scatter(x[clusters==2,0], x[clusters==2,1], s=75, c="green")
plt.show()

dendrogram = sch.dendrogram(sch.linkage(x, method="ward"))
plt.show()