import sqlite3
import pandas as pd
import os

# Configuration
DB_PATH = "fintech_analytics.db"
EXPORT_PATH = "data/processed"

# Export query to CSV
def export_to_csv(conn, query, filename):
    df = pd.read_sql_query(query, conn)
    filepath = os.path.join(EXPORT_PATH, filename)
    df.to_csv(filepath, index=False)
    print(f"  exported {len(df)} rows to {filename}")
    return df

# Main
def main():
    print("Connecting to database...")
    conn = sqlite3.connect(DB_PATH)

    os.makedirs(EXPORT_PATH, exist_ok=True)

    print("\nExporting tables for Power BI...")

    export_to_csv(conn, "SELECT * FROM dim_users", "dim_users.csv")

    export_to_csv(conn, "SELECT * FROM fct_transactions", "fct_transactions.csv")

    export_to_csv(conn, "SELECT * FROM fct_monthly_spending", "fct_monthly_spending.csv")

    export_to_csv(conn, """
        SELECT
            acquisition_channel,
            COUNT(DISTINCT user_id)                     AS total_users,
            ROUND(SUM(amount), 2)                       AS total_spend,
            ROUND(SUM(amount) / COUNT(DISTINCT user_id), 2) AS spend_per_user
        FROM fct_transactions
        WHERE is_debit = 1
        GROUP BY acquisition_channel
        ORDER BY spend_per_user DESC
    """, "acquisition_performance.csv")

    export_to_csv(conn, """
        SELECT
            risk_segment,
            COUNT(user_id)                  AS total_users,
            ROUND(AVG(credit_score), 0)     AS avg_credit_score,
            ROUND(AVG(balance), 2)          AS avg_balance,
            ROUND(AVG(overdraft_count), 2)  AS avg_overdrafts
        FROM dim_users
        GROUP BY risk_segment
        ORDER BY total_users DESC
    """, "risk_summary.csv")

    conn.close()
    print("\nAll exports complete. Files saved to data/processed/")

if __name__ == "__main__":
    main()