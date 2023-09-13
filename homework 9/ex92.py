#Generate n=100 random points in a unit square [0,1]x[0,1]. 
#Points are green if the distance from (0,0) is less then 1; they are red otherwise. 
#The marker area of a point (x,y) should be proportional to |x|+|y|.

import matplotlib.pyplot as plt
import numpy as np

# Wygenerowanie punktów
n = 100
x_points = np.random.rand(n)
y_points = np.random.rand(n)

# obliczenie dystansu i ustawienie koloru
distances = np.sqrt(x_points**2 + y_points**2)

color = []
for d in distances:
    if d < 1: color.append('green')
    else: color.append('red')

marker_areas = np.abs(x_points) + np.abs(y_points)

#utworzenie wykresu
plt.scatter(x_points, y_points, c=color, s=marker_areas*10)
plt.xlabel('X')
plt.ylabel('Y')

plt.show()