
-- 1. Top 5 Funds by AUM

SELECT
    d.scheme_name,
    d.fund_house,
    f.aum_crore
FROM fact_performance f
JOIN dim_fund d
ON f.amfi_code = d.amfi_code
ORDER BY f.aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Month

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', date)
ORDER BY month;


-- 3. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- 4. Funds with Expense Ratio < 1%

SELECT
    d.scheme_name,
    d.fund_house,
    p.expense_ratio_pct
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code = d.amfi_code
WHERE p.expense_ratio_pct < 1
ORDER BY p.expense_ratio_pct ASC;


--- 5. for SIP YoY growth

WITH monthly_sip AS (
    SELECT
        strftime('%Y', transaction_date) AS year,
        strftime('%m', transaction_date) AS month,
        SUM(amount_inr) AS total_sip
    FROM fact_transactions
    WHERE transaction_type = 'SIP'
    GROUP BY
        strftime('%Y', transaction_date),
        strftime('%m', transaction_date)
)

SELECT
    year,
    month,
    ROUND(total_sip, 2) AS total_sip,
    ROUND(
        (
            total_sip -
            LAG(total_sip, 12) OVER (ORDER BY year, month)
        ) * 100.0 /
        LAG(total_sip, 12) OVER (ORDER BY year, month),
        2
    ) AS yoy_growth_pct
FROM monthly_sip
ORDER BY
    year,
    month;


-- 6. Average Return by Risk Grade

SELECT
    risk_grade,
    ROUND(AVG(return_1yr_pct), 2) AS avg_1yr_return,
    ROUND(AVG(return_3yr_pct), 2) AS avg_3yr_return,
    ROUND(AVG(return_5yr_pct), 2) AS avg_5yr_return
FROM fact_performance
GROUP BY risk_grade
ORDER BY avg_5yr_return DESC;


-- 7. Top 5 Fund Houses by Number of Schemes

SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC
LIMIT 5;


-- 8. Average NAV by Fund House

SELECT
    d.fund_house,
    ROUND(AVG(n.nav), 2) AS average_nav
FROM fact_nav n
JOIN dim_fund d
ON n.amfi_code = d.amfi_code
GROUP BY d.fund_house
ORDER BY average_nav DESC;


-- 9. Total Investment Amount by Payment Mode

SELECT
    payment_mode,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_investment
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_investment DESC;


-- 10. Highest Rated Mutual Funds

SELECT
    d.scheme_name,
    d.fund_house,
    p.morningstar_rating,
    p.return_5yr_pct
FROM fact_performance p
JOIN dim_fund d
ON p.amfi_code = d.amfi_code
WHERE p.morningstar_rating = 5
ORDER BY p.return_5yr_pct DESC;

