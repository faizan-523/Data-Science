import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

print("After Filling Missing Values:")
new_df = df.fillna({
    'Age':0,
    'City':'Unknown',
    'Salary':0.0
})

print(new_df)

print("After Interpolation:")
new_df = df.interpolate()
print(new_df)

print("After Dropping Missing Values:")
new_df = df.dropna()
print(new_df)

d = pd.DataFrame({
    'Name': ['Ali', 'Ahmed', 'Faizan', 'Rafay'],
    'Score': ['A', 'B', 'C', 'D']} 
)

new_d = d.replace({'Score': {'A': 90, 'B': 80, 'C': 70, 'D': 60}})
print(new_d)

