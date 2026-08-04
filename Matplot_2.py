import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([10, 15, 25, 20])
y2 = np.array([5, 10, 15, 10])
y3 = np.array([2, 5, 10, 8])#Bar chart
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
