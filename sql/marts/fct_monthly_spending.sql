-- Fact table: monthly spending
-- Aggregated spending by user, month, and category
-- Powers trend analysis and business KPI reporting

CREATE VIEW fct_monthly_spending AS
SELECT
    user_id,
    transaction_month,
    transaction_year,
    category,
    account_type,
    acquisition_channel,
    state,

    -- Spending metrics
    COUNT(transaction_id) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_spend,
    ROUND(AVG(amount), 2) AS avg_transaction_amount,
    MAX(amount) AS largest_transaction

FROM fct_transactions
WHERE
    is_debit = 1

GROUP BY
    user_id,
    transaction_month,
    transaction_year,
    category,
    account_type,
    acquisition_channel,
    state;