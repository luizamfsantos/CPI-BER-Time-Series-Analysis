import numpy as np
import matplotlib.pyplot as plt

def plot_time_series(x, y, color='navy', title='Monthly CPI', label='t', ylabel='CPI'):
    plt.figure(figsize=(8, 6))
    if isinstance(y, list):
        for idx, line_data in enumerate(y):
            if isinstance(color, list):
                line_color = color[idx] if idx < len(color) else color[-1]
            else:
                line_color = color
            plt.plot(x, line_data, color=line_color, linewidth=2.5, label=label[idx] if isinstance(label, list) else label)
    else:
        plt.plot(x, y, color=color, linewidth=2.5, label=label)

    plt.title(title)
    plt.xlabel('t')
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

