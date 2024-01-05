""" THPT - 2021, BN """
import numpy as np
import matplotlib.pyplot as plt
import random


def f_(a, x):
    """ evaluate the function f given its explicit algebraic formula"""
    return a * x ** 4 - (a + 2) * x ** 2 - 3


def plot_(a, x):
    """ plot the graph for a specific value 'a' """
    plt.plot(x, f_(a, x),
             color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),         # rgb
             linewidth=2, label=f"a = {a}")


plt.figure(figsize=(8, 6))
plt.xlim(-2, 2)
plt.xticks(np.linspace(-2, 2, 9))
plt.axhline(color="grey", linewidth=0.3)
plt.xlabel('x')

plt.ylim(-7, 7)
plt.yticks(np.linspace(-7, 7, 15))
plt.axvline(color="grey", linewidth=0.3)
plt.ylabel('y')

plt.grid(color="grey", linewidth=0.3, linestyle="dotted")

vect_x = np.linspace(-2, 2, 100)
for a_ in [0.5, 1, 2, 3, 4]:
    plot_(a_, vect_x)
# show that f(x) + 4 = 0 has 4 solutions
plt.plot(vect_x, -4 * np.ones(len(vect_x)),
         color="red", linestyle="dotted", linewidth=2,
         label="y = -4")

plt.legend(loc="best", fontsize=14)
# show the maximal point (0, -3)
plt.scatter(0, -3, color='red', label='Maximal Point')
plt.annotate('maximal', xy=(0, -3), xytext=(0 + 0.1, -3 + 0.5),
             arrowprops=dict(facecolor='black', arrowstyle="->"))
title_font = {'fontsize': 14,
              'fontfamily': 'Arial',
              'fontstyle': 'italic'       # 'normal', 'italic', 'oblique'
              }
plt.title(r"$y = a x^{4} - (a + 2) x^{2} - 3$" + "\n", fontdict=title_font)
plt.show()
plt.savefig("function_plotter2.svg")
