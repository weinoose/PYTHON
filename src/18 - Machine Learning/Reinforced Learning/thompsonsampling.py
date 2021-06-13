import math
import random
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ucb.csv")

n0 = len(data.index.tolist())
d0 = len(data.columns.tolist())

ones = [0] * d0
zeros = [0] * d0
clicks = [0] * d0 
toplam = 0 
chosen = []
for n in range(1,n0):
    ad = 0
    max_th = 0
    for i in range(0,d0):
        ranbeta = random.betavariate(ones[i] +1, zeros[i] + 1)
        if ranbeta > max_th:
            max_th = ranbeta
            ad = i
    chosen.append(ad)
    clicks[ad] = clicks[ad]+ 1
    award = data.values[n,ad]
    if award == 1:
        ones[ad] += 1
    else:
        zeros[ad] += 1
    toplam = toplam + award

plt.hist(chosen, range(0, d0+1), histtype='bar', rwidth=0.75, color="red")
plt.title(f"Total: {toplam}")
plt.show()