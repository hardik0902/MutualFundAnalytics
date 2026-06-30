import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print(df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# Data Quality - Ok

df.to_csv("data/processed/cleaned_fund_master.csv",index=False)