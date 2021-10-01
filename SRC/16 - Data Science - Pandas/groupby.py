import pandas as pd

file = pd.read_csv("goldenfoot.csv")
df = pd.DataFrame(file)

# Creating a new dataset which rows are not spesific COLUMN'S VALUES given as a parameter.
data = df.groupby("Year")
print(data.min())