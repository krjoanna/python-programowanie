#Plot functions sin(x), cos(x), and exp(-x) in a range [0,10] in the same figure. 
#Colors are red, green, and blue, respectively. 
#Lines are solid, dashed, and dotted, respectively. Add a legend.

import numpy as np
import matplotlib.pyplot as plt

#wygenerowanie wartości [0,10]
x = np.linspace(0, 10)

#obliczenie wartości funkcji
sin_val = np.sin(x)
cos_val = np.cos(x)
exp_val = np.exp(-x)

#stworzenie figury z 3 wykresami
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Plot sin(x) with a red solid line in the first subplot
axs[0].plot(x, sin_val, color='red', linestyle='solid', label='sin(x)')
axs[0].set_title('sin(x)')
axs[0].legend()

# Plot cos(x) with a green dashed line in the second subplot
axs[1].plot(x, cos_val, color='green', linestyle='dashed', label='cos(x)')
axs[1].set_title('cos(x)')
axs[1].legend()

# Plot exp(-x) with a blue dotted line in the third subplot
axs[2].plot(x, exp_val, color='blue', linestyle='dotted', label='exp(-x)')
axs[2].set_title('exp(-x)')
axs[2].legend()

plt.show()
