import pandas as pd

file = pd.read_csv("goldenfoot.csv")
df = pd.DataFrame(file)
data = df.groupby("Year").min()

# Sorting values according to a specific column which givan as a parameter.
print(data.sort_values("Goals", ascending=False), "\n")
# Finding the max value according to a specific column which givan as a parameter.
print(data["Goals"].max(), "\n")
# Finding the min value of the specific column which givan as a parameter.
print(data["Goals"].min(), "\n")
# Summing the whole value according to a specific column which givan as a parameter.
print(data["Goals"].sum(), "\n")
# Finding the mean value of the specific column which givan as a parameter.
print(data["Goals"].mean(), "\n")
# Counting the value of the specific column which givan as a parameter.
print(data["Goals"].count(), "\n")
# Sorting the indexing with using ascending=True. 
print(data.sort_index(), "\n")
# Getting the row which has the MOST GOALS.
record = data.loc[data["Goals"] == data["Goals"].max()]
print(record)

# DATA ANALYSIS MESSAGE

string = f'\nIn the last decade; {list(record["Winner"])[0]} scored {list(record["Goals"])[0]} goals in a single season {list(record["Team"])[0]} in the league.\nThat makes {list(record["Winner"])[0]} had the record which is most goals in a single season recorded at his domestic league.'
print(string)

# DATA ANALYSIS MESSAGE vol.2

string = f"\nTotal goals by award winners in the last decade:\n"
print(string)
soccer_list = list(set(list(df["Winner"])))
dictionary = {}
for i in soccer_list:
    dictionary[i] = data.loc[data['Winner'] == i]['Goals'].sum()

serie = pd.Series(dictionary)
print(serie.sort_values(ascending=False))