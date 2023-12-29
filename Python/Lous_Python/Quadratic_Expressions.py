"""Module 01- 06: Quadratic Equations """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def f_(a, b, c, x):
    """ quadratic expression """
    return a * x ** 2 + b * x + c


def plot_parabola(a, b, c, ax):
    """ plot the parabola with its vertex and line of symmetry in a given ax"""
    # coordinates of the vertex
    vertex_x = (-b) / (2 * a)
    vertex_y = f_(a, b, c, vertex_x)
    # symmetric x - range about vertex_x
    min_x, max_x = vertex_x - 10, vertex_x + 10
    # table of x & y values
    df = pd.DataFrame({'x': np.linspace(min_x, max_x, 41)})
    df['y'] = f_(a, b, c, df['x'])
    # y - range
    min_y, max_y = df['y'].min(), df['y'].max()

    # parabola
    ax.axhline(color='black', linewidth=1)
    ax.axvline(color='black', linewidth=1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(color='grey', linestyle='dashed', linewidth=0.3)
    ax.plot(df.x, df.y,
            color="grey", marker="o", markersize=3)
    # Annotate the equation of the graph
    equation = f"y = {a}x \N{SUPERSCRIPT TWO} + {b}x + {c}"
    ax.annotate(equation, (max_x, max_y),
                rotation=60 * np.sign(a), ha='right', va='top')
    # vertex
    ax.scatter(vertex_x, vertex_y, color="red", linewidths=5, marker="*")
    ax.annotate('vertex', (vertex_x, vertex_y),
                xytext=(vertex_x - 1, (vertex_y + 5) * np.sign(a)))
    # line of symmetry
    ax.plot([vertex_x, vertex_x], [min_y, max_y], color="lightblue")
    ax.text(vertex_x - 1, (min_y + max_y) / 2,
            'Line of Symmetry', rotation=90, ha='right', va='center')


# create subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# On the left side, plot a parabola with a > 0
axs[0].set_title('Parabola with a > 0')
plot_parabola(2, 2, -4, axs[0])
# On the right side, plot a parabola with a < 0
axs[1].set_title('Parabola with a < 0')
plot_parabola(-2, 3, 5, axs[1])

plt.tight_layout()
plt.show()
