import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('random_data_ds.xlsx')

#Bar Chart
plt.bar(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Bar Chart of Salary by Age')
plt.show()

#Histogram
plt.hist(df['Salary'],  bins=10,
                        edgecolor='black',
                        color='tan',
                        alpha=0.7,
                        linewidth=1.2)
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Histogram of Salary')
plt.show()
