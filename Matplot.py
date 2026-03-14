import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([10, 15, 25, 20])
y2 = np.array([5, 10, 15, 10])
y3 = np.array([2, 5, 10, 8])

plt.title("Line Plot", fontsize=20,
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

plt.grid(color='gray', 
         linestyle='--', 
         linewidth=1)

plt.show()

#Bar chart
cat = ['Chocolate', 'Vanilla', 'Strawberry', 'Mint','Lemon', 'Blueberry']
values = [20, 15, 25, 10, 5, 30]

plt.bar(cat, values, color=[ 'tan'])

plt.title("Bar Chart", fontsize=20,
                        family='Arial',
                        fontweight='bold',
                        color='Black')

plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()

plt.pie(values, labels=cat,
                autopct='%1.1f%%', 
                colors=['tan', 'lightblue', 'lightpink', 'lightgreen', 'lightyellow', 'lightcoral'])

plt.title("Pie Chart", fontsize=20,
                        family='Arial',
                        fontweight='bold',
                        color='Black')

plt.show()

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