#pd.merge(df1, df2, on="Columns_Name", how="type of join")

import pandas as pd

#customer dataframe
df_customer = pd.DataFrame({
    "CustomerID":[1, 2, 3],
    "Name":["Ramesh", "Suresh", "Kalpesh"]
})

#order dataframe
df_orders = pd.DataFrame({
    "CustomerID":[1, 2, 3],
    "OrderAmount":[250,450,350]
})

#merge
df_merged = pd.merge(df_customer, df_orders, on="CustomerID", how="inner")
print("inner join")
print(df_merged)