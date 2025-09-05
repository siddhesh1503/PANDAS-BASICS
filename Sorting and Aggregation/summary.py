'''
df["Column Name"].means()
df["Column Name"].sum()
df["Column Name"].max()
df["Column Name"].min()
'''

import pandas as pd

data = {
    "Name":["Arun", "Varun", "Karun"],
    "Age":[28, 4, 8],
    "Salary":[10000, 20000, 30000]
}

df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print("Mean of the Salary: ")
print(avg_salary)