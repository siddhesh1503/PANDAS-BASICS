''''
1 - how big is your datasets  
2 - what are the names of columns

shape and columns
'''
import pandas as pd

data ={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'Columns Names: {df.columns}')