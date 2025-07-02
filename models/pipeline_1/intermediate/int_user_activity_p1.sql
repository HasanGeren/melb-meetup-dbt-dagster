{{ config(
    materialized='dynamic_table',
    target_lag='1 minutes',
    on_configuration_change='apply',
    snowflake_warehouse='COMPUTE_WH'
) }}

SELECT
    e.event_id,
    e.user_id,
    c.subscription_type,
    e.event_type,
    e.event_time
FROM {{ ref('stg_app_events_p1') }} e
LEFT JOIN {{ ref('stg_customers_p1') }} c
    ON e.user_id = c.user_id
