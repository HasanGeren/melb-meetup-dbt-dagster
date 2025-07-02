# simulate_events.py
import os
import snowflake.connector
import random
import time
from datetime import datetime
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

# Snowflake connection settings
SNOWFLAKE_CONFIG = {
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA")
}

TABLES = ["RAW_APP_EVENTS_1", "RAW_APP_EVENTS_2"]
USERS = [1, 2, 3]
EVENT_TYPES = ["login", "logout", "purchase", "view"]

def get_connection():
    return snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG["user"],
        password=SNOWFLAKE_CONFIG["password"],
        account=SNOWFLAKE_CONFIG["account"],
        warehouse=SNOWFLAKE_CONFIG["warehouse"],
        database=SNOWFLAKE_CONFIG["database"],
        schema=SNOWFLAKE_CONFIG["schema"]
    )

def simulate_event():
    user_id = random.choice(USERS)
    event_type = random.choice(EVENT_TYPES)
    event_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    table = random.choice(TABLES)

    return table, (user_id, event_type, event_time)

def insert_event(cursor, table, event):
    cursor.execute(f"""
        INSERT INTO {table} (user_id, event_type, event_time)
        VALUES (%s, %s, %s)
    """, event)

if __name__ == "__main__":
    print("Starting Snowflake streaming simulation...")
    conn = get_connection()
    cursor = conn.cursor()

    try:
        while True:
            table, event = simulate_event()
            insert_event(cursor, table, event)
            conn.commit()
            print(f"Inserted into {table}: user_id={event[0]}, event_type={event[1]}, event_time={event[2]}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped simulation.")
    finally:
        cursor.close()
        conn.close()
