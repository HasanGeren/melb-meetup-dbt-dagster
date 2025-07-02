{{ config(
    materialized='dynamic_table',
    target_lag='1 minutes',
    on_configuration_change='apply',
    snowflake_warehouse='COMPUTE_WH'
) }}

WITH new_data AS (
    SELECT
        user_id,
        COUNT(*) AS total_events,
        COUNT(DISTINCT event_type) AS distinct_event_types,
        MAX(event_time) AS last_event_time
    FROM {{ ref('int_user_activity_p1') }}
    GROUP BY user_id
)

SELECT *
FROM new_data
