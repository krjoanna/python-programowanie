#Create the following NumPy arrays:


import numpy as np

#(a) float from 0.0 to 1.0 step 0.1, shape=(11,)
ArrayA = np.arange(0.0, 1.1, 0.1, dtype=np.float64)

print("Array (a): \n", ArrayA)

#(b) int zeros (1 byte) with shape=(5,6),
ArrayB = np.zeros((5, 6), dtype=np.int8)

print("Array (b): \n", ArrayB)

#(c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ..., x**8.

c = complex(0, 1)
ArrayC = np.power(c, np.arange(9))

print("Array (c): \n", ArrayC)
