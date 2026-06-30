import sqlite3
import pandas as pd
from sqlalchemy import create_engine
# SQLite will create a database named as bluestock_mf.db
conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

# making the table structure we have made to read
with open("sql/schema.sql", "r") as file:
    sql_script = file.read()

# now the table structure we have created are in bluestock_mf.db
cursor.executescript(sql_script)
conn.commit()

# now the whole database is created.
print("SQLite database created successfully.")


engine = create_engine("sqlite:///bluestock_mf.db")
fund_df = pd.read_csv("data/processed/cleaned_fund_master.csv")

nav_df = pd.read_csv("data/processed/cleaned_nav_history.csv")

transaction_df = pd.read_csv("data/processed/cleaned_investor_transactions.csv")

performance_df = pd.read_csv("data/processed/cleaned_schema_performance.csv")

aum_df = pd.read_csv("data/processed/cleaned_aum_by_fund_house.csv")

# loading the date to SQL database created table named as dim_fund
fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="append",
    index=False
)

print("dim_fund loaded successfully.")

print(pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    engine
))

print(pd.read_sql(
    "SELECT COUNT(*) AS total_rows FROM dim_fund;",
    engine
))

print(pd.read_sql(
    "SELECT * FROM dim_fund LIMIT 5;",
    engine
))

#now creating dim_date table 
# Convert date columns to datetime
fund_df["launch_date"] = pd.to_datetime(fund_df["launch_date"])

nav_df["date"] = pd.to_datetime(nav_df["date"])

transaction_df["transaction_date"] = pd.to_datetime(transaction_df["transaction_date"])

aum_df["date"] = pd.to_datetime(aum_df["date"])

all_dates = pd.concat([
    fund_df["launch_date"],
    nav_df["date"],
    transaction_df["transaction_date"],
    aum_df["date"]
])

all_dates = all_dates.drop_duplicates()
all_dates = all_dates.sort_values()
dim_date = pd.DataFrame({
    "date": all_dates
})
dim_date["day"] = dim_date["date"].dt.day

dim_date["month"] = dim_date["date"].dt.month

dim_date["quarter"] = dim_date["date"].dt.quarter

dim_date["year"] = dim_date["date"].dt.year

dim_date = dim_date.reset_index(drop=True)

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)
print("dim_date loaded successfully.")


# facts table
nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="append",
    index=False
)

print("fact_nav loaded successfully.")

transaction_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="append",
    index=False
)

print("fact_transactions loaded successfully.")

performance_fact = performance_df.drop(
    columns=[
        "scheme_name",
        "fund_house",
        "category",
        "plan"
    ]
)

performance_fact.to_sql(
    "fact_performance",
    engine,
    if_exists="append",
    index=False
)

print("fact_performance loaded successfully.")

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="append",
    index=False
)

print("fact_aum loaded successfully.")


tables = [
    "dim_fund",
    "dim_date",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

print("\n--- Row Count Verification ---")
for table in tables:
    query = f"SELECT COUNT(*) AS total_rows FROM {table};"

    result = pd.read_sql(query, engine)

    print(f"{table}")
    print(result)
    print("-" * 40)

conn.close()