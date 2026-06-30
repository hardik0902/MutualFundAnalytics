import pandas as pd

df = pd.read_csv("data/raw/05_category_inflows.csv")

print(df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# need to change the data types of the month column from string to datatime (YYYY-MM) format
df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

df.info()
# Data Quality - Ok

# now save the file in processed folder.
df.to_csv("data/processed/cleaned_category_inflows.csv",index=False)