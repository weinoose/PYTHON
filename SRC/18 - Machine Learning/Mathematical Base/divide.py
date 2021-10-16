import numpy as np

# Variables.

vx = np.array([5,10,15,20,25])
vy = np.array([1,2,3,4,5])
mx = np.array([[5,10,15,20,25],[30,35,40,45,50]])
my = np.array([[1,2,3,4,5],[6,7,8,9,10]])
tx = np.array([[[5,10,15,20,25],[30,35,40,45,50]],[[-5,-10,-15,-20,-25],[-30,-35,-40,-45,-50]]])
ty = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[-1,-2,-3,-4,-5],[-6,-7,-8,-9,-10]]])

# Array Divide.

def xdivide(x,y):
    assert len(x.shape)
    assert x.shape == y.shape

    x = x.copy()

    for i in range(x.shape[0]):
        x[i] /= y[i]
    return x

# Matrix Divide.

def mdivide(x,y):
    assert len(x.shape)
    assert x.shape == y.shape

    x = x.copy()

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] /= y[i,j]
    return x

# Tensor Divide.

def tdivide(x,y):
    assert len(x.shape)
    assert x.shape == y.shape

    x = x.copy()

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            for q in range(x.shape[2]):
                x[i,j,q] /= y[i,j,q]
    return x

def cvxcross(x,y):
    # X is Matrix.
    # Y is Vector.
    # Ndim Comprasion Always Have to be Like That : X > Y.
    # Vector values added seperately to each matrix columns.
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0]

    x = x.copy()

    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] /= y[j]
    return x

# RESULTS.

print(f"\n\nVX / VY\n{xdivide(vx,vy)}\nNdim: {vx.ndim}")
print(f"\n\nMX / MY\n{mdivide(mx,my)}\nNdim: {mx.ndim}")
print(f"\n\nTX / TY\n{tdivide(tx,ty)}\nNdim: {tx.ndim}")
print(f"\n\nMX / VX\n{cvxcross(mx,vx)}")