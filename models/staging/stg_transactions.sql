-- Staging model: transactions
-- Cleans and standardizes raw transaction data
-- Source: seeds/transactions.csv

with source as (
    select * from {{ ref('transactions') }}
),

staged as (
    select
        transaction_id,
        user_id,
        date(date) as transaction_date,
        lower(trim(merchant)) as merchant,
        lower(trim(category)) as category,
        amount,
        is_debit,
        lower(trim(status)) as status
    from source
    where
        transaction_id is not null
        and user_id is not null
        and status = 'completed'
)

select * from staged