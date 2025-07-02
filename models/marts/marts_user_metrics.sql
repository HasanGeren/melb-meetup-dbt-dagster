{{ config(materialized='incremental', unique_key='user_id') }}

SELECT
    user_id,
    COUNT(*) AS total_events,
    COUNT(DISTINCT event_type) AS distinct_event_types,
    MAX(event_time) AS last_event_time
FROM {{ ref('int_user_activity') }}
GROUP BY user_id
