import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,0.1,10)
print len(x)
y = np.exp( -(x - 0.5)*(x - 0.5))
plt.scatter(x,y)
plt.show()