import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# print(df.shape)
# print(df.isnull().sum())
# print(df.columns.tolist())
# df.info()
# print(df.head())

print("Duplicate AMFI Codes:", df["amfi_code"].duplicated().sum())

# return_columns = [
#     "return_1yr_pct",
#     "return_3yr_pct",
#     "return_5yr_pct",
#     "benchmark_3yr_pct",
#     "alpha",
#     "beta",
#     "sharpe_ratio",
#     "sortino_ratio",
#     "std_dev_ann_pct",
#     "max_drawdown_pct"
# ]

# # we will make a loop for each column 
# # and if any non numeric value occurs then error = "coerce" will change it into NaN
# for col in return_columns:
#     df[col] = pd.to_numeric(df[col], errors="coerce")

# print(df[return_columns].isnull().sum())

# # for find we will check for any negative values in the given below three columns.
# anomalies = df[
#     (df["return_1yr_pct"] < 0) | (df["return_3yr_pct"] < 0) | (df["return_5yr_pct"] < 0)
# ]

# if anomalies.empty:
#     print("No anomalies founded")
# else:
#     print(anomalies)

# # check expense ratio between 0.1 to 2.5 percent
# invalid_expense = df[(df['expense_ratio_pct']<0.1) | (df["expense_ratio_pct"]>2.5)]

# if invalid_expense.empty:
#     print("Requirement passed and no invalid expense ratio.")
# else:
#     print("Invalid expense ratios:")
#     print(invalid_expense)

# # removes duplicates if any
# df= df.drop_duplicates().reset_index(drop=True)

# df.to_csv("data/processed/cleaned_schema_performance.csv", index=False)
# print("Rows:", len(df))