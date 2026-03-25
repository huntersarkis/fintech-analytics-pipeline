-- STAGING: TRANSACTIONS
-- Cleans and standardizes raw transaction data
-- Filters out failed transactions
-- Standardizes text fields to lowercase for consistency

CREATE VIEW stg_transactions AS
SELECT
    transaction_id,
    user_id,
    DATE(date) AS transaction_date,
    LOWER(TRIM(merchant)) AS merchant,
    LOWER(TRIM(category)) AS category,
    ROUND(amount, 2) AS amount,
    is_debit,
    LOWER(TRIM(status)) AS status,

    -- Derived field: year and month for aggregations
    STRFTIME('%Y', date) AS transaction_year,
    STRFTIME('%Y-%m', date) AS transaction_month

FROM raw_transactions
WHERE
    transaction_id IS NOT NULL
    AND user_id IS NOT NULL
    AND date IS NOT NULL
    AND status != 'failed';