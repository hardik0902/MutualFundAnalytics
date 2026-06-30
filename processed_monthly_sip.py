import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print(df.shape)
print(df.head())
df.info()
print(df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# as month column in str format so we have to change it to datetime format(YYYY-MM)
df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

# as we have seen the yoy_growth_pct have 12 null or NaN values then, 
print(df["yoy_growth_pct"].isnull().sum())
# since year on year growth has impact on business values and requirements and it needs data of same month in previous year
# so keep it as it is -

df.info()
# Data Quality - Ok

# now save the file in processed folder.
df.to_csv("data/processed/cleaned_monthly_sip_inflows.csv",index=False)