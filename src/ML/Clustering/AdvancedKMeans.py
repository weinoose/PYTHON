import pandas as pd
from kneed import KneeLocator
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns; sns.set_theme()
from sklearn.metrics import accuracy_score

data = pd.DataFrame(pd.read_excel("advancedkmeans.xlsx"))

data["RPN"] = data["Risk priortiy number"]
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

data["Cluster Values"] = list(x[clusters])
data["Cluster ID"] = list(clusters)
data = data.sort_values("RPN", ascending=False)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("SOD Cluster Result")

cvof = 0
cvoi = 0
ii = 0

colorlist = ["red","blue","green","yellow","black","purple","pink","brown"]

while ii < breakpoint:
    plt.scatter(x[clusters==cvoi+ii,0], x[clusters==cvoi+ii,1], s=100, c=colorlist[ii])
    ii += 1
plt.show()

seaborn_ax = sns.heatmap(x)
print(seaborn_ax)

variable = accuracy_score(clusters,km.predict(x))

rob = []
for i in list(data["Cluster ID"]):
    rob.append(colorlist[i])

data["Cluster Color"] = list(rob)

print(f"\nAccuracy: %{variable*100}\n")
print(f"Optimal Cluster Value: {breakpoint-1}\n")
print(f"Here is the list that defines the risks by critical to low critical using figuring risk id's:\n{data}")