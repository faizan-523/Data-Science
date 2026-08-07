import pandas as pd

df = pd.DataFrame({
    "Date": [
        "2026-08-01","2026-08-01","2026-08-01","2026-08-01","2026-08-01",
        "2026-08-02","2026-08-02","2026-08-02","2026-08-02","2026-08-02"
    ],

    "City": [
        "Karachi","Lahore","Islamabad","Quetta","Peshawar",
        "Karachi","Lahore","Islamabad","Quetta","Peshawar"
    ],

    "Temperature": [
        30,25,20,15,10,
        31,26,21,16,11
    ],

    "Humidity": [
        70,65,60,55,50,
        72,66,61,56,51
    ]
})

print(df)

print("\nPivot Table:\n")
p = df.pivot(index='Date', columns='City', values='Temperature')
print(p)

print("\nPivot Table:\n")
p = df.pivot_table(index='Date', columns='City', values='Temperature')
print(p)
