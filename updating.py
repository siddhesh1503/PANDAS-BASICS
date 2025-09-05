import pandas as pd

data ={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

# .loc[]
# df.loc[row_index, "Columns Name"] = new_value
# this use when specific element wants to update
df.loc[0, "Salary"] = 55000
print(df)