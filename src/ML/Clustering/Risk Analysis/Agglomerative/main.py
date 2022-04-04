import pandas as pd
from kneed import KneeLocator
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns; sns.set_theme()
from sklearn.cluster import AgglomerativeClustering

data = pd.DataFrame(pd.read_excel("main.xlsx"))
data["RPN"] = data["Risk priortiy number"]
data = data.drop(axis=1, columns=["Risk priortiy number"])

x = data[["S","D","O"]].values

distance = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k, random_state=1)
    km = km.fit(x)
    distance.append(km.inertia_)
plt.plot(K, distance, 'or--', c = 'red')
plt.xlabel('Values Of K')
plt.ylabel('Distortion')
plt.title('The Elbow Method Using Distortion')
plt.show()

x_values = list(K)
y_values = distance

kene = KneeLocator(x_values,y_values, curve='convex', direction='decreasing', interp_method='interp1d')
breakpoint = kene.knee

agg = AgglomerativeClustering(n_clusters = 5, affinity="euclidean", linkage="ward")
clusters = agg.fit_predict(x)

colorlist = ["purple","red","green","blue","yellow"]

plt.title("Agglomerative Hierarchical Clustering")
plt.scatter(x[clusters==0,0], x[clusters==0,1], s=50, c=colorlist[0])
plt.scatter(x[clusters==1,0], x[clusters==1,1], s=50, c=colorlist[1])
plt.scatter(x[clusters==2,0], x[clusters==2,1], s=50, c=colorlist[2])
plt.scatter(x[clusters==3,0], x[clusters==3,1], s=50, c=colorlist[3])
plt.scatter(x[clusters==4,0], x[clusters==4,1], s=50, c=colorlist[4])
plt.xlabel("Severity")
plt.ylabel("Density")
plt.title("SOD Cluster Result")
plt.show()

seaborn_ax = sns.heatmap(x)
print(seaborn_ax)

data["Cluster Values"] = list(x[clusters])
data["Cluster ID"] = list(clusters)
data = data.sort_values("RPN", ascending=False)

rob = []
for i in list(data["Cluster ID"]):
    if i > 4:
        rob.append(colorlist[4])
    else:
        rob.append(colorlist[i])

data["Cluster Color"] = list(rob)

deg_list, deg, deg_lvl = ['Critical Risk','Very High Risk','Medium Risk', 'Low Risk', 'High Risk'], [], []

for i in list(data['Cluster ID']):
    if i >= 4:
        deg.append(deg_list[4])
    else:
        deg.append(deg_list[i])

data['Risk Degree'] = deg
data = data.drop(axis=1, columns=["Cluster ID"])
data = data.set_index('Risk ID')

for i in list(data['Risk Degree']):
    if i == 'Critical Risk':
        deg_lvl.append(5)
    elif i == 'Very High Risk':
        deg_lvl.append(4)
    elif i == 'High Risk':
        deg_lvl.append(3)
    elif i == 'Medium Risk':
        deg_lvl.append(2)
    elif i == 'Low Risk':
        deg_lvl.append(1)

data['Risk Level Out Of 5'] = deg_lvl
data = data.drop(axis=1, columns=["RPN"])
print(f"Optimal Cluster Value: {breakpoint}\n")
print(f"Here is the list that defines the risks by critical to low critical using figuring risk id's:\n{data.sort_values('Risk Level Out Of 5', ascending=False)}")