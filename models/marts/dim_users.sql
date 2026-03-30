-- Mart model: dim_users
-- One row per user with account attributes and risk segment
-- Depends on: stg_users, stg_account_balances

with users as (
    select * from {{ ref('stg_users') }}
),

account_balances as (
    select * from {{ ref('stg_account_balances') }}
),

joined as (
    select
        u.user_id,
        u.name,
        u.email,
        u.state,
        u.account_type,
        u.acquisition_channel,
        u.signup_date,
        u.is_active,
        u.days_since_signup,
        ab.balance,
        ab.credit_score,
        ab.overdraft_count,

        -- Risk segment logic
        case
            when ab.credit_score >= 750 and ab.overdraft_count = 0 then 'low'
            when ab.credit_score >= 650 and ab.overdraft_count <= 2 then 'medium'
            else 'high'
        end as risk_segment

    from users u
    left join account_balances ab on u.user_id = ab.user_id
)

select * from joined