{{ config(
    materialized='dynamic_table',
    target_lag='1 minutes',
    on_configuration_change='apply',
    snowflake_warehouse='COMPUTE_WH'
) }}


SELECT
    event_id,
    user_id,
    event_type,
    event_time
FROM {{ source('demo_schema', 'raw_app_events_2') }}
WHERE event_time >= dateadd('hour', -2, current_timestamp())
