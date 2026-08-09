import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Name": [
        "Ali", "Ahmed", "Sara", "Hamza", "Ayesha",
        "Usman", "Hina", "Bilal", "Zain", "Fatima",
        "Saad", "Maham", "Danish", "Iqra", "Hassan"
    ],

    "Age": [
        20, 21, 19, 22, 20,
        23, 21, 24, 19, 22,
        25, 20, 21, 23, 20
    ],

    "Salary": [
        45000, 50000, 48000, 52000, 47000,
        55000, 51000, 49000, 53000, 50000,
        56000, 54000, 52000, 200000, 51000
    ],

    "Experience": [
        1, 2, 1, 3, 2,
        4, 2, 5, 1, 3,
        6, 2, 3, 4, 1
    ],

    "Marks": [
        72, 85, 78, 91, 69,
        88, 76, 95, 81, 74,
        89, 77, 84, 93, 15
    ]
})

print(df)

Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
print("Outliers:", outliers)

mean_salary = df['Salary'].mean()
print("Mean Salary:", mean_salary)

std = df['Salary'].std()
print("Standard Deviation:", std)

df['Z_Score'] = (df['Salary'] - mean_salary) / std
z_score_threshold = 3

outliers_z_score = df[(df['Z_Score'] < -z_score_threshold) | (df['Z_Score'] > z_score_threshold)]
print("Outliers based on Z-Score:\n", outliers_z_score)

sns.boxplot(x=df['Salary'])
plt.title("Boxplot of Salary")
plt.show()