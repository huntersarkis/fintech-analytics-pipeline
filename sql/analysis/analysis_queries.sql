-- Analysis queries: fintech analytics pipeline
-- These queries surface business insights from the mart layer
-- Each query answers a specific business question

-- _______________________________________________
-- 1. Top spending categories by total volume
-- Which categories are driving the most spend?
-- _______________________________________________

SELECT
    category,
    COUNT(transaction_id) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_spend,
    ROUND(AVG(amount), 2) AS avg_spend
FROM fct_transactions
WHERE is_debit = 1
GROUP BY category
ORDER BY total_spend DESC;


-- _______________________________________________
-- 2. Top merchants by transaction volume
-- Which merchants are most popular among users?
-- _______________________________________________

SELECT
    merchant,
    category,
    COUNT(transaction_id) AS transaction_count,
    ROUND(SUM(amount), 2) AS total_spend
FROM fct_transactions
WHERE is_debit = 1
GROUP BY merchant, category
ORDER BY transaction_count DESC
LIMIT 10;


-- _______________________________________________
-- 3. Acquisition channel performance
-- Which channels bring in the highest spending users?
-- _______________________________________________

SELECT
    acquisition_channel,
    COUNT(DISTINCT user_id) AS total_users,
    COUNT(transaction_id) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_spend,
    ROUND(SUM(amount) /
        COUNT(DISTINCT user_id), 2) AS spend_per_user
FROM fct_transactions
WHERE is_debit = 1
GROUP BY acquisition_channel
ORDER BY spend_per_user DESC;


-- _______________________________________________
-- 4. Monthly spending trends
-- How does total spend change month over month?
-- _______________________________________________

SELECT
    transaction_month,
    COUNT(DISTINCT user_id) AS active_users,
    COUNT(transaction_id) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_spend
FROM fct_transactions
WHERE is_debit = 1
GROUP BY transaction_month
ORDER BY transaction_month ASC;


-- _______________________________________________
-- 5. Customer risk breakdown
-- How many users fall into each risk segment?
-- _______________________________________________

SELECT
    risk_segment,
    COUNT(user_id) AS total_users,
    ROUND(AVG(credit_score), 0) AS avg_credit_score,
    ROUND(AVG(balance), 2) AS avg_balance,
    ROUND(AVG(overdraft_count), 2) AS avg_overdrafts
FROM dim_users
GROUP BY risk_segment
ORDER BY total_users DESC;


-- _______________________________________________
-- 6. Spending by account type
-- Do premium users spend more than checking or savings?
-- _______________________________________________

SELECT
    account_type,
    COUNT(DISTINCT user_id) AS total_users,
    ROUND(SUM(amount), 2) AS total_spend,
    ROUND(AVG(amount), 2) AS avg_transaction_amount,
    ROUND(SUM(amount) /
        COUNT(DISTINCT user_id), 2) AS spend_per_user
FROM fct_transactions
WHERE is_debit = 1
GROUP BY account_type
ORDER BY spend_per_user DESC;