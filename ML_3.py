import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df =pd.DataFrame({
    'Mileage': [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
    'age': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Price': [20000, 18000, 15000, 12000, 10000, 8000, 6000, 4000, 2000, 1000]
})


X = df[['Mileage', 'age']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

reg = LinearRegression()
reg.fit(X_train, y_train)

y_pred = reg.predict(X_test)
print("Predicted prices for test set: ", y_pred)

score = reg.score(X_test, y_test)
print("Model  score: ", score)

print("Intercept:", reg.intercept_)
print("Coefficients:", reg.coef_)

