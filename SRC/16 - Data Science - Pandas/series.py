import pandas as pd
import numpy as np

# Data Setting.

dictionary = {"A":1, "B":2, "C":3}
result = pd.Series(dictionary)
print(result)

# Data Setting 2.

numbers = [1,2,3]
letters = ["A", "B", "C"]
result = pd.Series(numbers, letters)
print(result)

# Data Settings 3.

numbers = np.random.randint(0,10,3)
letters = ["A","B","C"]
result = pd.Series(numbers, letters)
print(result)

# Column Methods.

print(result.ndim)
print(result.shape)
print(result.max())
print(result.min())
print(result.sum())

# Column Indexing.

print(result[1])
print(result[-1])
print(result[::])