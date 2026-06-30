# Mutual Fund Analytics 
# Data Dictionary

## Project Overview

This data dictionary documents the tables, columns, data types, business definitions, and source files used in the Mutual Fund Analytics SQLite database.

# Table: dim_fund

Stores master information about every mutual fund scheme.

# FROM --  cleaned_fund_master.csv

| Column | Data Type | Business Definition |
|---------|-----------|---------------------|
| amfi_code | INTEGER | Unique AMFI code for each mutual fund scheme |
| scheme_name | TEXT | Name of the mutual fund scheme |
| fund_house | TEXT | Mutual fund company |
| category | TEXT | Fund category (Equity, Debt, Hybrid etc.) |
| sub_category | TEXT | Detailed classification of the scheme |
| plan | TEXT | Growth/Direct/Regular plan |
| launch_date | DATE | Scheme launch date |
| benchmark | TEXT | Benchmark index used for comparison |
| expense_ratio_pct | REAL | Annual expense ratio (%) |
| exit_load_pct | REAL | Exit load percentage |
| min_sip_amount | REAL | Minimum SIP investment amount |
| min_lumpsum_amount | REAL | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | Risk category assigned to the scheme |
| sebi_category_code | TEXT | SEBI classification code |

---

# Table: dim_date

Stores calendar information used by all fact tables.

# FROM -- Generated from cleaned datasets.

| Column | Data Type | Business Definition |
|---------|-----------|---------------------|
| date | DATE | Calendar date |
| day | INTEGER | Day of month |
| month | INTEGER | Month number |
| quarter | INTEGER | Quarter number |
| year | INTEGER | Calendar year |

---

# Table: fact_nav

Stores daily Net Asset Value (NAV) for each scheme.

# FROM -- cleaned_nav_history.csv

| Column | Data Type | Business Definition |
|---------|-----------|---------------------|
| amfi_code | INTEGER | Mutual fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

# Table: fact_transactions

Stores investor transaction details.

# FROM -- cleaned_investor_transactions.csv

| Column | Data Type | Business Definition |
|---------|-----------|---------------------|
| transaction_id | INTEGER | Auto-generated unique transaction ID |
| investor_id | INTEGER | Investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Mutual fund identifier |
| transaction_type | TEXT | SIP, Lumpsum or Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | City classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income (Lakhs) |
| payment_mode | TEXT | Mode of payment |
| kyc_status | TEXT | Investor KYC status |

---

# Table: fact_performance

Stores fund performance and risk metrics.

# FROM -- cleaned_schema_performance.csv

| Column | Data Type | Business Definition |
|---------|-----------|---------------------|
| amfi_code | INTEGER | Mutual fund identifier |
| return_1yr_pct | REAL | One-year return (%) |
| return_3yr_pct | REAL | Three-year return (%) |
| return_5yr_pct | REAL | Five-year return (%) |
| benchmark_3yr_pct | REAL | Benchmark return (%) |
| alpha | REAL | Alpha performance metric |
| beta | REAL | Beta risk measure |
| sharpe_ratio | REAL | Risk-adjusted return |
| sortino_ratio | REAL | Downside risk-adjusted return |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown (%) |
| aum_crore | INTEGER | Assets Under Management (Crores) |
| expense_ratio_pct | REAL | Annual expense ratio (%) |
| morningstar_rating | INTEGER | Morningstar rating (1–5) |
| risk_grade | TEXT | Overall fund risk grade |

---

# Table: fact_aum

Stores Assets Under Management (AUM) by fund house.

# FROM -- cleaned_aum_by_fund_house.csv

| Column | Data Type | Business Definition |
|---------|-----------|---------------------|
| date | DATE | Reporting date |
| fund_house | TEXT | Mutual fund company |
| aum_lakh_crore | REAL | AUM in lakh crores |
| aum_crore | INTEGER | AUM in crores |
| num_schemes | INTEGER | Number of schemes managed |

---

## Primary Keys

| Table | Primary Key |
|--------|-------------|
| dim_fund | amfi_code |
| dim_date | date |
| fact_nav | (amfi_code, date) |
| fact_transactions | transaction_id |
| fact_performance | amfi_code |
| fact_aum | (date, fund_house) |

---

## Foreign Keys

| Child Table | Foreign Key | Parent Table |
|--------------|-------------|--------------|
| fact_nav | amfi_code | dim_fund |
| fact_nav | date | dim_date |
| fact_transactions | amfi_code | dim_fund |
| fact_transactions | transaction_date | dim_date |
| fact_performance | amfi_code | dim_fund |
| fact_aum | date | dim_date |
