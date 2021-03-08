import numpy as np

result = np.array([1,3,5,7,9]) # Creating an array.
result = np.arange(1,10) # Creating an range array.
result = np.arange(10,100,3) # Creating an range array x by x.
result = np.zeros(10) # Creating an "0." array for x times.
result = np.ones(10) # Creating an "1." array for x times.
result = np.linspace(0,100,5) # Creating a range array y by y.
np_array = np.arange(50) # Creating a range array.
result = np_array.reshape(5,10) # Shaping the array to 5 rows and 10 columns.
result = result.ndim # Shows the matrix size.
result = np.random.randint(10,100,6) # Selecting randomly count of z values between x and y.

arrr = np.array([1, 5, 7])

result = arrr.mean()
result = arrr.min()
result = arrr.max()

print(result)