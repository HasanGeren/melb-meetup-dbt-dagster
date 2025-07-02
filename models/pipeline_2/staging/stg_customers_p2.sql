{{ config(materialized='view') }}

SELECT
    user_id,
    name,
    subscription_type,
    signup_date
FROM {{ source('demo_schema', 'raw_customers_2') }}
