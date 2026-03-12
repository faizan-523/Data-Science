import pandas as pd

#series
s = pd.Series([1, 3, 5, 7, 9])
print(s)

#dataframe
df = pd.DataFrame({"names": ['Faizan', 'Ahmed', 'Ali'],
                   "marks": [85, 95, 90]})
print(df)

#reading data
data = pd.read_excel('random_data_ds.xlsx')
print(data.head())
print(data)
print(data.describe())
print(data.info())

#data selection
print(data['Name'])
print(type(data['Name']))
print(data[['Name', 'Age']])
print(data.iloc[0])
print(data.iloc[0:3])
print(type(data.iloc[0]))

