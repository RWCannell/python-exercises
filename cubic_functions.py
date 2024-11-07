import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-7, 4, 50)

def f(x):
    return x**3 + 6*x**2 - x - 30

y = f(x)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.plot(2, f(2), "bo")
plt.annotate("(2, 0)", (2, -15), color="blue")

plt.plot(-3, f(-3), "bo")
plt.annotate("(-3, 0)", (-3, 10), color="blue")

plt.plot(-5, f(-5), "bo")
plt.annotate("(-5, 0)", (-5, -15), color="blue")

plt.plot(0, -30, "bo")
plt.annotate("(0, -30)", (0.25, -40), color="blue")

plt.plot(-4.08, f(-4.08), "ro")
plt.annotate("(-4.08, 6.04)", (-6, 12), color="red")

plt.plot(0.08, f(0.08), "ro")
plt.annotate("(0.08, -30.04)", (-0.75, -20), color="red")

plt.xlabel("x")
plt.ylabel("y")

plt.plot(x, y, color="blue")
plt.annotate("f(x) = x^3 + 6x^2 - x - 30", (-1, 100), color="blue")

plt.show() 