{{ config(
    materialized='incremental',
    unique_key='user_id'
) }}

WITH new_data AS (
    SELECT
        user_id,
        COUNT(*) AS total_events,
        COUNT(DISTINCT event_type) AS distinct_event_types,
        MAX(event_time) AS last_event_time
    FROM {{ ref('int_user_activity') }}
    {% if is_incremental() %}
    WHERE event_time > (SELECT MAX(last_event_time) FROM {{ this }})
    {% endif %}
    GROUP BY user_id
)

SELECT *
FROM new_data
