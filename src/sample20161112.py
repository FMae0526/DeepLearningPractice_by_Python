import numpy as np
import matplotlib.pyplot as plt

# Making Data
x = np.arange(0, 6, 0.1)        # Making From 0 to 6 by 0.1
y = np.sin(x)


# Drawing Graph
plt.plot(x, y)
plt.show

