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

