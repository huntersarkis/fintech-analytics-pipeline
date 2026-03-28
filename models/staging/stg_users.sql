-- Staging model: users
-- Cleans and standardizes raw user data
-- Source: seeds/users.csv

with source as (
    select * from {{ ref('users') }}
),

staged as (
    select
        user_id,
        lower(trim(name)) as name,
        lower(trim(email)) as email,
        lower(trim(state)) as state,
        lower(trim(account_type)) as account_type,
        lower(trim(acquisition_channel)) as acquisition_channel,
        date(signup_date) as signup_date,
        is_active,

        -- Derived field: days since signup
        date_diff(date('2024-12-31'), date(signup_date), day) as days_since_signup

    from source
    where
        user_id is not null
        and email is not null
        and signup_date is not null
)

select * from staged