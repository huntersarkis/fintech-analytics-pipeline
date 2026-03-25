-- STAGING: ACCOUNT BALANCES
-- Cleans and standardizes raw account balance data
-- Flags users at financial risk based on credit score and overdraft history

CREATE VIEW stg_account_balances AS
SELECT
    user_id,
    LOWER(TRIM(account_type)) AS account_type,
    ROUND(balance, 2) AS balance,
    credit_score,
    overdraft_count,
    DATE(snapshot_date) AS snapshot_date,

    -- Derived field: risk flag
    CASE
        WHEN credit_score < 650
        AND overdraft_count >= 2 THEN 'high_risk'
        WHEN credit_score < 700
        OR  overdraft_count >= 1 THEN 'medium_risk'
        ELSE 'low_risk'
    END AS risk_segment

FROM raw_account_balances
WHERE
    user_id IS NOT NULL
    AND balance IS NOT NULL
    AND credit_score IS NOT NULL;