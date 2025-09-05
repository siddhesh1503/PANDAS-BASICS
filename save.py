import pandas as pd

data = {
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[10, 20, 30],
    "City":['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)
print(df)

df.to_csv("ouput.csv", index=False)
#df.to_json("ouput.json", index=False)