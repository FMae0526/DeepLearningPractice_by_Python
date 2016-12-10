
import numpy as np
import matplotlib.pyplot as plt

# Making Date
x = np.arange(0, 6, 0.1)	# Making from 0 to 6 by 0.1
y1 = np.sin(x)
y2 = np.cos(x)


# Drawing Graph
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--",label="sin")	# Draw by Wave
plt.xlabel("x")		# Label of x
plt.ylabel("y")		# Label of y
plt.title('sin & cos')	# Title
plt.legend()
plt.show()
