{{ config(materialized='materialized_view') }}

SELECT
    event_id,
    user_id,
    event_type,
    event_time
FROM {{ source('demo_schema', 'raw_app_events') }}
