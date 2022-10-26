import pandas as pd
from kneed import KneeLocator
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns; sns.set_theme()

data = pd.DataFrame(pd.read_excel("main.xlsx"))
data["RPN"] = data["Risk priortiy number"]
data = data.drop(axis=1, columns=["Risk priortiy number"])

x = data[["S","O","D"]].values
distance = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k, random_state=1)
    km = km.fit(x)
    distance.append(km.inertia_)
plt.plot(K, distance, 'or--', c = 'green')
plt.xlabel('Values Of K')
plt.ylabel('Distortion')
plt.title('The Elbow Method Using Distortion')
plt.show()

x_values = list(K)
y_values = distance

kene = KneeLocator(x_values,y_values, curve='convex', direction='decreasing', interp_method='interp1d')
breakpoint = kene.knee

km = KMeans(n_clusters = 5, init = "k-means++", random_state = 17)
clusters = km.fit_predict(x)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("SOD Cluster Result")

cvof = 0
cvoi = 0
ii = 0

colorlist = ["green","purple","blue","red","yellow","black"]

while ii < breakpoint:
    plt.scatter(x[clusters==cvoi+ii,0], x[clusters==cvoi+ii,1], s=100, c=colorlist[ii])
    ii += 1
plt.show()

seaborn_ax = sns.heatmap(x)
print(seaborn_ax)

data["Cluster Values"] = list(x[clusters])
data["Cluster ID"] = list(clusters)
data = data.sort_values("RPN", ascending=False)

rob = []
for i in list(data["Cluster ID"]):
    if i > 5:
        rob.append(colorlist[5])
    else:
        rob.append(colorlist[i])

data["Cluster Color"] = list(rob)

deg_list, deg, deg_lvl = ['Medium Risk','Critical Risk','Low Risk','Very High Risk','High Risk','Deadly Risk'], [], []

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

data['Risk Degree'] = deg
data['Risk Level Out Of 5'] = deg_lvl
data = data.drop(axis=1, columns=["RPN"])
print(f"Optimal Cluster Value: {breakpoint}\n")
print(f"Here is the list that defines the risks by critical to low critical using figuring risk id's:\n{data.sort_values('Risk Level Out Of 5', ascending=False)}")