import math
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ucb.csv")

n0 = len(data.index.tolist())
d0 = len(data.columns.tolist())

awards = [0] * d0 
clicks = [0] * d0 
toplam = 0 
chosen = []
for n in range(1,n0):
    ad = 0
    max_ucb = 0
    for i in range(0,d0):
        if(clicks[i] > 0):
            ortalama = awards[i] / clicks[i]
            delta = math.sqrt(3/2* math.log(n)/clicks[i])
            ucb = ortalama + delta
        else:
            ucb = n0*10
        if max_ucb < ucb:
            max_ucb = ucb
            ad = i          
    chosen.append(ad)
    clicks[ad] = clicks[ad]+ 1
    award = data.values[n,ad]
    awards[ad] = awards[ad]+ award
    toplam = toplam + award

plt.hist(chosen, range(0, d0+1), histtype='bar', rwidth=0.75, color="red")
plt.title(f"Total: {toplam}")
plt.show()