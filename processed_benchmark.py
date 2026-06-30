import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print(df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# need to change the data types of the date column from string to datatime format
df["date"] = pd.to_datetime(df["date"])

df.info()
# Data Quality - Ok

# now save the file in processed folder.
df.to_csv("data/processed/cleaned_benchmark_indices.csv",index=False)