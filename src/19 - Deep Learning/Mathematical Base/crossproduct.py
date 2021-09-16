import math
import numpy as np

v1 = np.array([3,2,2])
v2 = np.array([1,4,2])

def ParallelogramArea(a,b):
    area = math.sqrt((a[1] * b[2] - b[1] * a[2]) ** 2 + (a[0] * b[2] - b[0] * a[2]) ** 2 + (a[0] * b[1] - b[0] * a[1]) ** 2)
    return area

print(f"\n\nV1 to V2 Cross Product\n{np.cross(v1,v2)}")
print(f"\n\nV2 to V1 Cross Product\n{np.cross(v2,v1)}")
print(f"\n\nArea of Parallelogram Made by V1/V2 Vectors\n{'%.2f' % ParallelogramArea(v1,v2)}")

"""

MATHEMATICAL PROOF

v1 = [3,2,2]
v2 = [1,4,2]

CROSS(v1,v2) = [(2*2-4*2), -(3*2-1*2), (3*4-1*2)]
RESULT = [-4, -4, 10]

"""