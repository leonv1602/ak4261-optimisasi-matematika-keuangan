import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.3,0.4,1000)
y = (2*(1+x)**15-(1+x)**25 - 1)/(2*(1+x)**15-(1+x)**17 - (1+x)**5) - 0.5636
plt.plot(x,y)
plt.grid(True)
plt.show()