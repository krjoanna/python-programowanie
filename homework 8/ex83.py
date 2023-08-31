
import numpy as np

#(a) Create a two dimensional array called m1, shape=(4,5).

m1 = np.array([[100, 200, 300, 400, 500],[600, 700, 800, 900, 1000],
              [1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])

#(b) Create a new array m2 from m1, in which the elements of each row are in reverse order.

# (b) Create a new array m2 from m1, with reversed elements in each row.
m2 = np.array([row[::-1] for row in m1])

#(c) Create a new array m3 from m1, in which the elements of each column are in reverse order.
m3 = np.array([col[::-1] for col in m1.T]).T

#(d) Cut of the first and last row and the first and last column of m1.
m4 = m1[1:-1, 1:-1]

print("Array m1:\n", m1)
print("\nArray m2 (rows reversed):\n", m2)
print("\nArray m3 (columns reversed):\n", m3)
print("\nArray m4 (trimmed):\n", m4)
