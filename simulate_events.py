import psycopg2
import random
import time
from datetime import datetime, timedelta

# Database connection settings
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    dbname="demo_db",
    user="demo_user",
    password="demo"
)
cursor = conn.cursor()

users = [1, 2, 3]
event_types = ['login', 'logout', 'purchase', 'view']

def simulate_event():
    user_id = random.choice(users)
    event_type = random.choice(event_types)
    event_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("""
        INSERT INTO demo_schema.raw_app_events (user_id, event_type, event_time)
        VALUES (%s, %s, %s)
    """, (user_id, event_type, event_time))
    conn.commit()

    print(f"Inserted event: user_id={user_id}, event_type={event_type}, event_time={event_time}")

# Simulate event every 1 seconds
try:
    print("Starting streaming simulation...")
    while True:
        simulate_event()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped simulation.")
finally:
    cursor.close()
    conn.close()
