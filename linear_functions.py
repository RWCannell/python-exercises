import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 10)

def f(x):
    return 3*x + 9

y = f(x)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.plot(-3, f(-3), "go")
plt.annotate("(-3, 0)", (-3, f(-3) - 3), color="green")

plt.plot(0, f(0), "go")
plt.annotate("(0, 9)", (0.75, f(0) - 0.5), color="green")

plt.xlabel("x")
plt.ylabel("y")

plt.plot(x, y, color="green")
plt.annotate("f(x) = 3x + 9", (3, f(3) + 15), color="green")

plt.show() 