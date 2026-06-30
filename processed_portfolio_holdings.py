import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print(df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# need to change the data types of the portolio date column from string to datatime format
df["portfolio_date"] = pd.to_datetime(df["portfolio_date"])

df.info()
# Data Quality - Ok

# now save the file in processed folder.
df.to_csv("data/processed/cleaned_portfolio_holdings.csv",index=False)