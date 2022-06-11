import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np


def plot(labels, data1, data2, title, x_label, y_label, legend1, legend2, path, log=False):
    figure(figsize=(20, 6), dpi=80)
    title = title + " " + "(Line Plot)"

    plt.plot(labels, data1, label=legend1, linestyle="-")
    plt.plot(labels, data2, label=legend2, linestyle="-")

    x = np.linspace(min(labels),max(labels),100)
    y1 = x**3
    y2 = (x**2) * np.log2(x)

    coeff = max(y1) / max(data1)
    y1 = y1 / coeff
    y2 = y2 / coeff

    plt.plot(x, y1, 'b', label="x^3", linestyle="--")
    plt.plot(x, y2, 'r', label="x^2 * log(x)", linestyle="--")
    
    plt.xlabel(x_label, labelpad=15, fontsize=12, color="#333533")
    plt.ylabel(y_label, labelpad=15, fontsize=12, color="#333533")
    if log==True:
        plt.yscale('log')  # logarithmic scale

    plt.title(title, fontsize=18, color="#333533", pad=35)

    # removing axes from the figure
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.legend(loc='upper center', ncol=2, frameon=False)

    ticks = list(map(int, labels))
    ticks.insert(0, 0)
    plt.xticks(ticks)

    plt.savefig(path)
    plt.show()