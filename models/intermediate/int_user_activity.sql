{{ config(
    materialized='incremental',
    unique_key='event_id'
) }}

SELECT
    e.event_id,
    e.user_id,
    c.subscription_type,
    e.event_type,
    e.event_time
FROM {{ ref('stg_app_events') }} e
LEFT JOIN {{ ref('stg_customers') }} c
    ON e.user_id = c.user_id
{% if is_incremental() %}
WHERE e.event_time > (SELECT MAX(event_time) FROM {{ this }})
{% endif %}
