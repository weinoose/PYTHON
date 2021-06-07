import numpy as np

# Mathematical Operators.

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

result = np.sin(numbers1)
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(np.array([2.7, 10])) # Log base defined for euler number.

print(result)

# Array Stacking.

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
print(mnumbers2)

result = np.vstack((mnumbers1, mnumbers2))
result = np.hstack((mnumbers1, mnumbers2))

print(result)

# Mathematical Comparing.

result = numbers1 >= 50
print(numbers1[result])