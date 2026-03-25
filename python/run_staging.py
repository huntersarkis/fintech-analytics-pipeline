import sqlite3
import os

# Configuration
DB_PATH = "fintech_analytics.db"
STAGING_PATH = "sql/staging"

STAGING_FILES = [
    "stg_users.sql",
    "stg_transactions.sql",
    "stg_account_balances.sql"
]

# Run sql file
def run_sql_file(conn, filepath):
    with open(filepath, "r") as f:
        sql = f.read()
    conn.executescript(sql)
    print(f"  executed: {filepath}")

# Drop existing views
def drop_existing_views(conn):
    views = ["stg_users", "stg_transactions", "stg_account_balances"]
    for view in views:
        conn.execute(f"DROP VIEW IF EXISTS {view}")
    conn.commit()
    print("  existing staging views dropped")

# Verify views
def verify_views(conn):
    cursor = conn.cursor()
    views = ["stg_users", "stg_transactions", "stg_account_balances"]
    print("\nVerifying staging views...")
    for view in views:
        cursor.execute(f"SELECT COUNT(*) FROM {view}")
        count = cursor.fetchone()[0]
        print(f"  {view}: {count} rows")

# Main
def main():
    print("Connecting to database...")
    conn = sqlite3.connect(DB_PATH)

    print("\nDropping existing staging views...")
    drop_existing_views(conn)

    print("\nRunning staging SQL files...")
    for filename in STAGING_FILES:
        filepath = os.path.join(STAGING_PATH, filename)
        run_sql_file(conn, filepath)

    verify_views(conn)

    conn.close()
    print("\nStaging layer complete.")

if __name__ == "__main__":
    main()