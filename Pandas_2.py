import pandas as pd

df = pd.DataFrame({
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', 
            '1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', 
            '1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017'],
    'city': ['new york', 'new york', 'new york', 'new york', 
             'mumbai', 'mumbai', 'mumbai', 'mumbai', 
             'paris', 'paris', 'paris', 'paris'],
    'temperature': [32, 36, 28, 33, 90, 85, 87, 92, 45, 50, 54, 42],
    'windspeed': [6, 7, 12, 7, 5, 12, 15, 5, 20, 13, 8, 10],
    'event': ['Rain', 'Sunny', 'Snow', 'Sunny', 
              'Sunny', 'Fog', 'Fog', 'Rain', 
              'Sunny', 'Cloudy', 'Cloudy', 'Cloudy']
})

print(df)

g = df.groupby('city')

print("Grouped DataFrame:")
for city, city_df in g:
    print(city)
    print(city_df)

print("Maximum values for each group:")
print(g.max())

print("Description for each group:")
print(g.describe())