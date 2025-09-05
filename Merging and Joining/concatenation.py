'''
vertically (row-wise)
horizontally (Column-wise)

pd.concate(df1, df2), axis=0, ignore_index=True)

[df1, df2] =
axis = 1

ignore_index = True

'''

import pandas as pd

#region1
df_region1 = pd.DataFrame({
    "CustomerID": [1,2],
    "Name": ["Gopal", "Raju"]
})

#region2
df_region2 = pd.DataFrame({
    "CustomerID": [3,4],
    "Name": ["Shyam", "Raju"]
})

#concatenate vertically
df_concat = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print(df_concat)