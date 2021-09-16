import numpy as np

numbers = np.arange(0,25,5) # Creating a array like = [0 5 10 15 20]

result = numbers[4] # Input Parameter = Index Value, Output Parameter = Element.
result = numbers[-1] # Shows last element of the array.
result = numbers[0:3] # Shows between a and b indexes.
result = numbers[::] # Shows the whole array.
result = numbers[::3] # Shows the whole array three by three.
result = numbers[1,5] # Shows the x'th array's y'th element.

print(result)