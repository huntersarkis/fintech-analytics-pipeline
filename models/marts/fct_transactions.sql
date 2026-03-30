with transactions as (
    select * from {{ ref('stg_transactions') }}
),

users as (
    select * from {{ ref('dim_users') }}
),

joined as (
    select
        t.transaction_id,
        t.user_id,
        u.name,
        u.state,
        u.account_type,
        u.acquisition_channel,
        u.risk_segment,
        t.transaction_date,
        t.merchant,
        t.category,
        t.amount,
        t.is_debit,
        t.status
    from transactions t
    left join users u on t.user_id = u.user_id
)

select * from joined