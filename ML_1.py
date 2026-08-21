import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.DataFrame({
    'area': [2600, 3000, 3200, 3600, 4000],
    'price': [550000, 565000, 610000, 680000, 725000]
})

plt.scatter(df['area'], df['price'], marker='o')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('House Price vs Area')
plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['area']], df['price'])

predict = reg.predict([[3300]])
print("Predicted price for area 3300 sq ft: ", predict)
