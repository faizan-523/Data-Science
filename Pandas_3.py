import pandas as pd

pak_weather = pd.DataFrame({
    "City": ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"],
    "Temperature": [30, 25, 20, 15, 10],
    "Humidity": [70, 65, 60, 55, 50]
})

us_weather = pd.DataFrame({
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Temperature": [20, 25, 15, 30, 35],
    "Humidity": [60, 55, 65, 70, 50]
})
print("After Concatenation:")
df = pd.concat([pak_weather, us_weather], keys=["Pakistan", "USA"])
print(df)

