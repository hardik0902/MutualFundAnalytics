import pandas as pd

# to read the CSV file - NAV HISTROY 
df = pd.read_csv("data/raw/02_nav_history.csv")

print(df.shape)
# print(df.head())
print(df.columns.tolist())

# # firstly we need to know there are any missing values, duplicates and validate NAV > 0
# print("Total Missing Values:\n",(df.isnull().sum()))

# print()
# # now for duplicate rows
# print("Duplicate Rows : ", df.duplicated().sum())

# print()
# # for validating NAV > 0
# print("NAV values <=0 : ", ((df["nav"] <= 0).sum()))

# now we will do the functions - 

# 1. convert date to datetime format
df["date"] = pd.to_datetime(df["date"])

# 2. sorting the data according to AMFI_CODE + DATE
df = df.sort_values(["amfi_code", "date"])

# 3. remove duplicates - 
df = df.drop_duplicates()

# forward fill NAVs within each fund 
# and also dates were in order as we have already sorted the AMFI Codes
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# now validate are there any NAV <= 0 or the condition is NAV must be greater than 0
df = df[df["nav"]>0]

# now we will save this file in processed folder
# index = false as we don't want serial no. column to be present in csv file

df.to_csv("data/processed/cleaned_nav_history.csv", index = False)
print("\nClean NAV history CSV file uploaded\n")
print("Rows:", len(df))
print(df.info())