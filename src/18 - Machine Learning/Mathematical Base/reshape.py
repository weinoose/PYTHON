import numpy as np

# Variables.

v = np.array([1,2,3,4,5,6])
m = np.array([[1,2,3,4,5,6],[6,7,8,9,10,11]])
t = np.array([[[1,2,3,4,5,6],[6,7,8,9,10,11]],[[-1,-2,-3,-4,-5,-6],[-6,-7,-8,-9,-10,-11]]])

# Reshaping a vector.

v = v.reshape(3,2) # X * Y must be equal to total lenght of the vector!
print(f"\n\nVector to Matrix\n{v}")

v = v.reshape(1,2,3) # X * Y must be equal to total lenght of the vector!
print(f"\n\nVector to Tensor\n{v}")

# Reshaping a matrix.

m = m.reshape(6,2) # X * Y must be equal to total lenght of the matrix!
print(f"\n\nMatrix to Matrix\n{m}")

m = m.reshape(3,2,2) # X * Y must be equal to total lenght of the matrix!
print(f"\n\nMatrix to Tensor\n{m}")

# Reshaping a tensor.

t = t.reshape(3,4,2) # X * Y must be equal to total lenght of the matrix!
print(f"\n\nTensor to Tensor\n{t}")

t = t.reshape(6,4) # X * Y must be equal to total lenght of the matrix!
print(f"\n\nTensor to Matrix\n{t}")

t = np.array(t.reshape(24,1).flatten(), ndmin=1) # X * Y must be equal to total lenght of the matrix!
print(f"\n\nTensor to Vector\n{t}")