""" the graph of y = (4x^3 - 6x^2 + 1) * sqrt{x + 1} / (3 - x) where -1 <= x <= 1.5 """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def f_(x):
    """ function f(x) """
    return (4 * x ** 3 - 6 * x ** 2 + 1) * np.sqrt(x + 1) / (3 - x)


df = pd.DataFrame({'x': np.linspace(-1, 1.5, 200)})
df['y'] = f_(df['x'])
plt.axhline(color="black", linewidth=0.5)
plt.xlabel('x')
plt.axvline(color="black", linewidth=0.5)
plt.ylabel('y')
plt.plot(df.x, df.y, color="red", linewidth=3)
plt.xlim(-1, 1.5)
plt.xticks(np.linspace(-1, 1.4, 13))
plt.ylim(-1, 1.5)
plt.yticks(np.linspace(-1, 1.4, 13))
plt.grid(color="grey", linewidth=0.3, linestyle="dotted")
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica"
})
plt.title(r"$y = \dfrac{(4 x^{3} - 6x^{2} + 1) \sqrt{x + 1}}{(3 - x)}$")
plt.tight_layout()
plt.show()
