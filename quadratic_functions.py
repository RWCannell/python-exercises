import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 5, 100)

def f(x):
    return 2*x**2 + 12*x + 10

y = f(x)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.plot(-5, f(-5), "mo")
plt.annotate("(-5, 0)", (-5, 4), color="magenta")

plt.plot(-1, f(-1), "mo")
plt.annotate("(-1, 0)", (-2, 6), color="magenta")

plt.plot(-3, -8, "mo")
plt.annotate("(-3, -8)", (-2.5, -12), color="magenta")

plt.xlabel("x")
plt.ylabel("y")

plt.plot(x, y, color="magenta")
plt.annotate("f(x) = 2x^2 + 12x + 10", (-8.75, f(-8.75) + 30), color="magenta")

plt.show() 