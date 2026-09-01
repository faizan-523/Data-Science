import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.DataFrame({
    'area': [2600, 3000, 3200, 3600, 4000],
    'bedrooms': [3, 4, 3, 5, 4],
    'age': [20, 15, 18, 30, 8],
    'price': [550000, 565000, 610000, 680000, 725000]
})

reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']], df['price'])

predict = reg.predict([[3300, 3, 15]])
print("Predicted price for area 3300 sq ft, 3 bedrooms, 15 years old: ", predict)
