import pandas as pd

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print(df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# need to change the data type of date from string to datetime format
df["date"] = pd.to_datetime(df["date"])
df.info()

# Data Quality - Ok

df.to_csv("data/processed/cleaned_aum_by_fund_house.csv",index=False)

