""" Src: https://en.wikipedia.org/wiki/File:Asymptote02_vectorial.svg
    Example of Guillaume Jacquenot
    a 2D- parametric curve (x(t), y(t)) where t > 0 with its asymptote
    The curve may intersect the asymptote an infinite amount of times.
"""
import numpy as np
import matplotlib.pyplot as plt


def plot_(t, n, output_filename=r'Asymptote02.svg'):
    """ plot the graph for a specific value 'n' """
    plt.figure(figsize=(8, 8))
    # plot the axis with tick marks of spacing 2
    plt.xlim(-6, 12)
    plt.xticks(range(-6, 13, 2))
    plt.xlabel(r'$x$')

    plt.ylim(-4, 12)
    plt.yticks(range(-4, 13, 2))
    plt.ylabel(r'$y$')

    plt.grid(color="grey", linewidth=0.3, linestyle="-")
    # plot the parametric curve
    plt.plot(t + np.cos(n * t) / t, t + np.sin(n * t) / t,
             color='#ee8d18', lw=2)
    # plot the asymptote
    plt.plot([-4, 12], [-4, 12], lw=1, ls='--', color='k')
    # plt.text(-4, -4, 'asymptote', rotation=45)
    plt.annotate('asymptote', xy=(-4, -4),
                 rotation=45, ha='center', va='bottom',   # ha = horizontally align, va = vertically align
                 fontsize=12, color='blue')
    # set xAxis:yAxis = 1: 1 (constrained scaling)
    plt.gca().set_aspect('equal')            # gca = get current axis
    title_font = {'fontsize': 14,
                  'fontfamily': 'serif',
                  'fontstyle': 'normal'  # 'normal', 'italic', 'oblique'
                  }
    plt.title(fr"$x = t + \dfrac{{\cos(nt)}}{{t}}, y = t + \dfrac{{\sin(nt)}}{{t}}, \quad t > 0, n = {n}$" + "\n",
              fontdict=title_font)
    plt.show()
    plt.savefig(output_filename)


t_ = np.arange(0.07, 12.0, 0.01)
plot_(t_, 14)
