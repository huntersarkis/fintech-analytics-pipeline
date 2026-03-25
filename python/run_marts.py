import sqlite3
import os

# Configuration
DB_PATH = "fintech_analytics.db"
MARTS_PATH = "sql/marts"

MART_FILES = [
    "dim_users.sql",
    "fct_transactions.sql",
    "fct_monthly_spending.sql"
]

# Run sql file
def run_sql_file(conn, filepath):
    with open(filepath, "r") as f:
        sql = f.read()
    conn.executescript(sql)
    print(f"  executed: {filepath}")

# Drop existing views
def drop_existing_views(conn):
    views = ["dim_users", "fct_transactions", "fct_monthly_spending"]
    for view in views:
        conn.execute(f"DROP VIEW IF EXISTS {view}")
    conn.commit()
    print("  existing mart views dropped")

# Verify views
def verify_views(conn):
    cursor = conn.cursor()
    views = ["dim_users", "fct_transactions", "fct_monthly_spending"]
    print("\nVerifying mart views...")
    for view in views:
        cursor.execute(f"SELECT COUNT(*) FROM {view}")
        count = cursor.fetchone()[0]
        print(f"  {view}: {count} rows")

# Main
def main():
    print("Connecting to database...")
    conn = sqlite3.connect(DB_PATH)

    print("\nDropping existing mart views...")
    drop_existing_views(conn)

    print("\nRunning mart SQL files...")
    for filename in MART_FILES:
        filepath = os.path.join(MARTS_PATH, filename)
        run_sql_file(conn, filepath)

    verify_views(conn)

    conn.close()
    print("\nMart layer complete.")

if __name__ == "__main__":
    main()