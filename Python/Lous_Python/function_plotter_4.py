""" THPT - 2021 - BN - C5, piecewise function
"""
import numpy as np
import matplotlib.pyplot as plt


def piecewise_function(x_):
    """ define a piecewise function of x """
    if -3 <= x_ <= 1:
        return -(x_ + 1) ** 2 + 1
    elif 1 <= x_ <= 3:
        return - 6 * (x_ - 2) ** 2 + 3


x = np.linspace(-3, 3, 100)
y = np.array([piecewise_function(_) for _ in x])
# plt.figure(figsize=(8, 8))
# plot the axis with tick marks of spacing 2
# plt.axis("off")        # remove the default axis = boxed

# plt.xlim(-4, 4)
plt.xticks(range(-4, 5))
plt.axhline(color="k")
plt.xlabel(r'$x$')

# plt.ylim(-3.2, 3.2)
plt.yticks(range(-3, 4))
plt.axvline(color="k")
plt.ylabel(r'$y$')

plt.grid(color="grey", linewidth=0.3, linestyle="--")
plt.plot(x, y, color='blue', lw=2)

data_x = np.linspace(-3, 3, 7)
data_y = [piecewise_function(x) for x in data_x]
plt.scatter(data_x, data_y,
            color='magenta', marker="o", s=50)

for i in range(len(data_x)):
    plt.vlines(data_x[i], ymin=0, ymax=data_y[i],
               linestyle='dashed', color='gray')
    plt.hlines(data_y[i], xmin=0, xmax=data_x[i],
               linestyle='dashed', color='gray')
# set xAxis:yAxis = 1: 1 (constrained scaling)
plt.gca().set_aspect('equal')            # gca = get current axis
title_font = {'fontsize': 14,
              'fontfamily': 'serif',
              'fontstyle': 'normal'  # 'normal', 'italic', 'oblique'
              }
plt.title("A piecewise function", fontdict=title_font)
plt.show()
