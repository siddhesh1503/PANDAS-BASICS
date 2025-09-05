#Sorting Data
#Sorting data in 1 column sort_values()
#df.sort_values(by="Column Name", True/False, inplace=True)

import pandas as pd

data = {
    "Name":["Arun", "Varun", "Karun"],
    "Age":[28, 4, 8],
    "Salary":[10000, 20000, 30000]
}

df = pd.DataFrame(data)

df.sort_values(by="Age", ascending=False, inplace=True)
print("Sorted age by Descending:")
print(df)