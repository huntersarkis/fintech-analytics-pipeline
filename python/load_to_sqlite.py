import pandas as pd
import sqlite3
import os

# Configuration
DB_PATH = "fintech_analytics.db"
RAW_DATA_PATH = "data/raw"

# Load CSV Files 
def load_csv(filename):
    path = os.path.join(RAW_DATA_PATH, filename)
    df = pd.read_csv(path)
    print(f"  Loaded {len(df)} rows from {filename}")
    return df

# Create database and load tables
def main():
    print("Connecting to SQLite database...")
    conn = sqlite3.connect(DB_PATH)

    print("\nLoading raw tables into SQLite...")

    users_df = load_csv("users.csv")
    users_df.to_sql("raw_users", conn, if_exists="replace", index=False)
    print("  raw_users table created")

    transactions_df = load_csv("transactions.csv")
    transactions_df.to_sql("raw_transactions", conn, if_exists="replace", index=False)
    print("  raw_transactions table created")

    balances_df = load_csv("account_balances.csv")
    balances_df.to_sql("raw_account_balances", conn, if_exists="replace", index=False)
    print("  raw_account_balances table created")

    # Verify
    print("\nVerifying row counts in database...")
    cursor = conn.cursor()
    for table in ["raw_users", "raw_transactions", "raw_account_balances"]:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  {table}: {count} rows")

    conn.close()
    print("\nDatabase created successfully at:", DB_PATH)

if __name__ == "__main__":
    main()