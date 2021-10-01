import random
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(pd.read_csv("ucb.csv"))

# n0 value is row count of the data.
n0 = len(data.index.tolist())
# d0 value is column count of the data
d0 = len(data.columns.tolist())

sum0 = 0
selected_ads = []

for n1 in range(0,n0):
  ad = random.randrange(d0)
  selected_ads.append(ad)
  award = data.values[n1,d0-1]
  sum0 += award

plt.hist(selected_ads, range(0, d0+1), histtype='bar', rwidth=0.75, color="red")
plt.title(f"Total: {sum0}")
plt.show()