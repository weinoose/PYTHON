import pandas as pd
from kneed import KneeLocator
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

data = pd.DataFrame(pd.read_excel("kmeans_advanced.xlsx"))

data["Risk Priority Number"] = data["Risk priortiy number"]
data = data.drop(axis=0, columns=["Risk priortiy number"])

x = data[["S","O","D"]].values

distance = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(x)
    distance.append(km.inertia_)

x_values = list(K)
y_values = distance

kene = KneeLocator(x_values,y_values, curve='convex', direction='decreasing', interp_method='interp1d')
breakpoint = kene.knee

km = KMeans(n_clusters = breakpoint, init = "k-means++", random_state = 17)
clusters = km.fit_predict(x)

plt.xlabel("SOD Cluster Result")
plt.ylabel("SOD Cluster Result")
plt.title("SOD Cluster Result")

cvof = 0
cvoi = 0
ii = 0

while ii < breakpoint:
    plt.scatter(x[clusters==cvoi+ii,0], x[clusters==cvoi+ii,1], s=100)
    ii += 1
plt.show()

variable = accuracy_score(clusters,km.predict(x))
print(f"Accuracy: %{variable*100}")
print(f"Optimal Cluster Value: {breakpoint}")