-- STAGING: USERS 
-- Cleans and standardizes raw user data
-- Filters out any records with missing critical fields
-- Standardizes text fields to lowercase for consistency

CREATE VIEW stg_users AS
SELECT
    user_id,
    LOWER(TRIM(email)) AS email,
    LOWER(TRIM(state)) AS state,
    LOWER(TRIM(account_type)) AS account_type,
    LOWER(TRIM(acquisition_channel)) AS acquisition_channel,
    DATE(signup_date) AS signup_date,
    is_active,

    -- Derived field: days since signup
    CAST(
        JULIANDAY('2024-12-31') - JULIANDAY(signup_date)
    AS INTEGER) AS days_since_signup

FROM raw_users
WHERE
    user_id IS NOT NULL
    AND email IS NOT NULL
    AND signup_date IS NOT NULL;