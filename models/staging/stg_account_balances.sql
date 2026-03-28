-- Staging model: account balances
-- Cleans and standardizes raw account balance data
-- Source: seeds/account_balances.csv

with source as (
    select * from {{ ref('account_balances') }}
),

staged as (
    select
        user_id,
        lower(trim(account_type)) as account_type,
        balance,
        credit_score,
        overdraft_count,
        date(snapshot_date) as snapshot_date
    from source
    where
        user_id is not null
)

select * from staged