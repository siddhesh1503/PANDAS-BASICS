import pandas as pd

data ={
    "Name":['Ram',None,'Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance":[85,None,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

# df.fillna(0, inplace=True)
# print(df)

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
df["Performance"].fillna(df["Performance"].mean(), inplace=True)
print(df)