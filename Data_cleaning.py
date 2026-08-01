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


