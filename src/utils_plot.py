import numpy as np
import matplotlib.pyplot as plt

def plot_time_series(x, y, color='navy', title='Monthly CPI', label='t', ylabel='CPI'):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color=color, linewidth=2.5, label=label)
    plt.title(title)
    plt.xlabel('t')
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
