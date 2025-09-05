import pandas as pd

#read data from CSV file into a dataframe
#df = pd.read_csv("C:\\Users\\91892\\Downloads\\sales_data_sample.csv", encoding="latin1")
df = pd.read_json("C:\\Users\\91892\\OneDrive\\Desktop\\PANDAS\\sample_Data.json")


print(df)