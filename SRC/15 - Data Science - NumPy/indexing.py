import numpy as np

numbers = np.arange(0,25,5) # Creating a array like = [0 5 10 15 20]

result = numbers[4] # Input Parameter = Index Value, Output Parameter = Element.
result = numbers[-1] # Shows last element of the array.
result = numbers[0:3] # Shows between a and b indexes.
result = numbers[::] # Shows the whole array.
result = numbers[::3] # Shows the whole array three by three.

numberx = np.array([[0,1,2],[3,4,5]])

result = numberx[1,0] # Shows the x'th array's y'th element.

print(result)