import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# print(df.shape)
# print(df.head())
# print(df.columns.tolist())
# print(df.isnull().sum())
print("Duplicate Investor IDs:", df["investor_id"].duplicated().sum())
print(df["investor_id"].nunique())
print(len(df))
# print("Transaction Types:")
# print(df["transaction_type"].value_counts())

# print("\nKYC Status:")
# print(df["kyc_status"].value_counts())

# print("\nAmount <= 0:")
# print((df["amount_inr"] <= 0).sum())

# print("\nTransaction Date Type:")
# print(df["transaction_date"].dtype)

# # change the data type
# df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# # standardization the type of transaction types
# df["transaction_type"] = df["transaction_type"].str.strip()

# df["transaction_type"] = df["transaction_type"].replace(
#     {
#         'sip' : 'SIP',
#         "Sip" : 'SIP',
#         'lumpsum' : 'Lumpsum',
#         'redemption' : 'Redemption'
#     }
# )
# # now all kind of transaction types as per standards - 
# print(df["transaction_type"].value_counts())
# # all types were checked and as per standards


# # validating KYC status - 
# valid_kyc = ["Verified", "Pending"]

# invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]
# print(invalid_kyc)
# it has been check that there are no any other kind of KYC status.

# to save the cleaned file in pre=ocessed folder
# df.to_csv("data/processed/cleaned_investor_transactions.csv", index=False)
# print("Cleaned transactions file has been put in processed folder.")

