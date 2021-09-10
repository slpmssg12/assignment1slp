import matplotlib.pyplot as plt

import numpy as np

t = np.linspace(-np.pi,np.pi)

plt.plot(t, np.sin(t), marker="+", label="sin", linestyle="-.")
plt.plot(t, np.cos(t), marker="^", label="cos", linestyle=":")

plt.title("sin & cos graph")
plt.xlabel("angle")
plt.ylabel("sin & cos value")
plt.legend()
plt.show()


