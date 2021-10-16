import numpy as np

# Definition of a Vector.

vector = np.array([1,3,5,7,9])
print(f"\n\nVECTOR\n{vector}\nndim: {vector.ndim}")

# Definition of a Matrix.

matrix = np.array([[1,3,5,7,9],[11,13,15,17,19]])
print(f"\n\nMATRIX\n{matrix}\nndim: {matrix.ndim}")

# Definition of a Tensor.

tensor = np.array([[[0,2,4,6,8],[10,12,14,16,18]],[[1,3,5,7,9],[11,13,15,17,19]]])
print(f"\n\nTENSOR\n{tensor}\nndim: {tensor.ndim}")