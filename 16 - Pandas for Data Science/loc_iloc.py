import pandas as pd

file = pd.read_csv("goldenfoot.csv")
df = pd.DataFrame(file)

# LOC takes STRING
# ILOC takes INTEGER

# Print's the whole information about spesific index given as a parameter. STRING TYPE
print(df.iloc[1])
# Print's the informations about spesific indexes given as a paramater. DATAFRAME type
print(df.iloc[0:2])

# Making a groupby operation to the DataFrame using LOC effectively.
df = df.groupby("Year").min()

# Print's the whole information about spesific index given as a parameter. DATAFRAME TYPE
print(df.loc[2011])
# Print's the informations about spesific indexes given as a paramater. DATAFRAME type
print(df.loc[2011:2013])
