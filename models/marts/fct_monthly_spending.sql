-- Mart model: fct_monthly_spending
-- Aggregated monthly spend by user, category, and channel
-- Depends on: fct_transactions

with transactions as (
    select * from {{ ref('fct_transactions') }}
),

monthly as (
    select
        date_trunc(transaction_date, month) as spending_month,
        user_id,
        name,
        account_type,
        acquisition_channel,
        risk_segment,
        category,
        count(transaction_id) as transaction_count,
        sum(amount) as total_amount
    from transactions
    where is_debit = 1
    group by 1, 2, 3, 4, 5, 6, 7
)

select * from monthly