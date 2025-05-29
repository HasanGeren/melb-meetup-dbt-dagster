from dagster import asset, AssetExecutionContext, Output
import psycopg2
from dagster import get_dagster_logger

logger = get_dagster_logger()

@asset
def refresh_stg_app_events(context: AssetExecutionContext):
    logger.info("Refreshing materialized view demo_schema.stg_app_events")

    conn = psycopg2.connect(
        dbname="demo_db",
        user="demo_user",
        password="demo",
        host="localhost",
        port=5433
    )
    cursor = conn.cursor()
    cursor.execute("REFRESH MATERIALIZED VIEW demo_schema.stg_app_events;")
    conn.commit()
    cursor.close()
    conn.close()

    logger.info("Refresh completed.")
    return Output(None)
