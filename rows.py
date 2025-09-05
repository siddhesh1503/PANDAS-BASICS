#head()  tail()
#head()  when you not specify the value it will show default 5 values
#trail() 5

import pandas as pd
df = pd.read_json("sample_Data.json")

print('Display 10 rows of first')
print(df.head(10))

print('Display 10 rows of last')
print(df.tail(10))