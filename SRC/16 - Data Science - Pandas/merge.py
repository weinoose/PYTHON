import pandas as pd

file = pd.read_csv("merge1.csv")
file2 = pd.read_csv("merge2.csv")
file3 = pd.read_csv("merge3.csv")

df = pd.DataFrame(file)
df2 = pd.DataFrame(file2)
df3 = pd.DataFrame(file3)

# DataFrame Append Method ( Common Columns Needed. )
result = pd.merge(df, df3, how="outer")
print(result)

# DataFrame Column Append Method
result = pd.concat([df,df2], axis = 1)
print(result)

# DataFrame Column Append Method ( OUTER APPEND WITH MISSING VALUES )
result = pd.concat([df,df2])
print(result)