-- Fact table: transactions
-- One row per transaction enriched with user attributes
-- Joins staging transactions with user dimension

CREATE VIEW fct_transactions AS
SELECT
    t.transaction_id,
    t.user_id,
    t.transaction_date,
    t.transaction_year,
    t.transaction_month,
    t.merchant,
    t.category,
    t.amount,
    t.is_debit,
    t.status,

    -- User attributes for segmentation
    u.state,
    u.account_type,
    u.acquisition_channel,
    u.risk_segment

FROM stg_transactions t
LEFT JOIN dim_users u
    ON t.user_id = u.user_id;