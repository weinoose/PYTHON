import pandas as pd

file = pd.read_csv("goldenfoot.csv")
df = pd.DataFrame(file)

# Prints the whole data.
print(df) 
# Prints the first x rows.
print(df.head(15))
# Prints the last x rows.
print(df.tail(15))
# Prints the whole columns as a list.
print(list(df.columns))
# Prints the whole row title's as a list.
print(list(df.index))
# Prints the whole values as a list and which values ordered in a spesific COLUMN given by a parameter. 
print(list(df["Winner"]))
# Prints the row and colun count of dataframe.
print(df.shape)
# Just prints the spesific column given by a parameter.
print(df["Winner"])
# Makes the spesific column's values into a numpy array.
print(df["Winner"].unique())