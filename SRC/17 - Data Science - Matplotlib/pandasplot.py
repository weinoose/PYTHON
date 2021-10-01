import pandas as pd
import matplotlib.pyplot as plt

# Gathering the data.
data = pd.read_csv("dataset.csv")
df = pd.DataFrame(data)

# Preparing the data.

names = []
values = []

for i in df.iloc:
    names.append(i[0])
    values.append(i[1])

print(names)
print(values)

# Making the plot.

plt.bar(names,values,label="F1 TOP TIER CHAMPIONS",width=.5)

plt.legend()
plt.xlabel("Drivers")
plt.ylabel("Championships")
plt.title("Formula 1 Championship")

plt.show()