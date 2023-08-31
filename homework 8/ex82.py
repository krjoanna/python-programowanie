import numpy as np

#(a) Create an arbitrary one dimensional array called v1.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v1 = np.array(list)

print("Array v1:\n", v1)

#(b) Create a new array v2 which consists of the odd indices of v1.
v2 = v1[1::2] #start:1 step:2

print("Array v2 (odd indices of v1 array):\n", v2)

#(c) Create a new array v3 in backwards ordering from v1.
v3 = v1[::-1]  # step: -1

print("Array v3 (backwards ordering from v1):\n", v3)


