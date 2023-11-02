import matplotlib.pyplot as plt
import numpy as npy

x = npy.linspace(-2 *npy.pi, 2* npy.pi, 100)
plt.plot(x, npy.sin(x), "r-o", label="sin(x)")
plt.plot(x, 0.6 * npy.cos(x), "b--", label="0.6*cos(x)")
plt.legend()
plt.xlabel("Rads")
plt.ylabel("Amplitude")
plt.title("Sine and Cosine Waves")
plt.show()