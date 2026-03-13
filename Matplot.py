import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([10, 15, 25, 20])
y2 = np.array([5, 10, 15, 10])
y3 = np.array([2, 5, 10, 8])

plt.title("Line Plott", fontsize=20,
                        family='Arial',
                        fontweight='bold',
                        color='Black')

plt.xlabel("Years", fontsize=15,
                    family='Arial',
                    fontweight='bold',
                    color='Black')
plt.ylabel("Numbers", fontsize=15,
                    family='Arial',
                    fontweight='bold',
                    color='Black')

plt.tick_params(axis='both',
                color='navy')

plt.plot(x,y1, marker='o',
         markersize=10,
         markerfacecolor='cyan',
         markeredgecolor='cyan',
         linestyle='solid',
         linewidth=4,
         color='navy')
plt.plot(x,y2, marker='o',
         markersize=10,
         markerfacecolor='magenta',
         markeredgecolor='magenta',
         linestyle='solid',
         linewidth=4,
         color='purple')
plt.plot(x,y3, marker='o',
         markersize=10,
         markerfacecolor='yellow',
         markeredgecolor='yellow',
         linestyle='solid',
         linewidth=4,
         color='orange')

plt.xticks(x)

plt.subplots_adjust(left=0.1, 
                    right=0.9, 
                    top=0.9, 
                    bottom=0.1)

plt.show()


