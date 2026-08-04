import matplotlib.pyplot as plt
import numpy as np

#Scatter Graph
x1 = np.array([0,1,2,3,4,5,6,7,7,8,9])
y1 = np.array([55,60,56,70,75,80,85,65,90,77,90])

plt.scatter(x1,y1)
plt.title("Scatter Graph",  fontsize=20,
                            family='Arial',
                            fontweight='bold',
                            color='Black')

plt.show()

scores = np.random.randint(0, 100, 50)
plt.hist(scores, bins=5, color='tan', edgecolor='black')
plt.title("Histogram", fontsize=20,
                        family='Arial',
                        fontweight='bold',
                        color='Black')
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.show()

#Subplots
x = np.array([1,2,3,4,5])

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, x*2, color='navy')
axs[0, 0].set_title("x*2", fontsize=15,
                            family='Arial',
                            fontweight='bold',
                            color='Black')

axs[0, 1].plot(x, x**2, color='purple')
axs[0, 1].set_title("x^2", fontsize=15,
                            family='Arial',
                            fontweight='bold',
                            color='Black')
axs[1, 0].plot(x, x**3, color='orange')
axs[1, 0].set_title("x^3", fontsize=15,
                            family='Arial',
                            fontweight='bold',
                            color='Black')
axs[1, 1].plot(x, np.sqrt(x), color='green')
axs[1, 1].set_title("sqrt(x)", fontsize=15,
                            family='Arial',
                            fontweight='bold',
                            color='Black')

plt.tight_layout()
plt.show()