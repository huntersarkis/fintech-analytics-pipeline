-- Dimension table: users
-- One row per user with clean attributes and risk segment
-- Joins staging users with account balance data

CREATE VIEW dim_users AS
SELECT
    u.user_id,
    u.email,
    u.state,
    u.account_type,
    u.acquisition_channel,
    u.signup_date,
    u.is_active,
    u.days_since_signup,

    -- Account attributes from balances staging
    b.balance,
    b.credit_score,
    b.overdraft_count,
    b.risk_segment

FROM stg_users u
LEFT JOIN stg_account_balances b
    ON u.user_id = b.user_id;