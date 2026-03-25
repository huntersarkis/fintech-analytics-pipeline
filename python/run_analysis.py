import sqlite3
import pandas as pd

# Configuration
DB_PATH = "fintech_analytics.db"

# Run query and print results
def run_query(conn, title, query):
    print(f"\n{title}")
    print("-" * 50)
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))
    return df

# Main
def main():
    print("Connecting to database...")
    conn = sqlite3.connect(DB_PATH)

    run_query(conn, "1. Top spending categories", """
        SELECT
            category,
            COUNT(transaction_id) AS transaction_count,
            ROUND(SUM(amount), 2) AS total_spend,
            ROUND(AVG(amount), 2) AS avg_spend
        FROM fct_transactions
        WHERE is_debit = 1
        GROUP BY category
        ORDER BY total_spend DESC
    """)

    run_query(conn, "2. Top 10 merchants by transaction volume", """
        SELECT
            merchant,
            category,
            COUNT(transaction_id) AS transaction_count,
            ROUND(SUM(amount), 2) AS total_spend
        FROM fct_transactions
        WHERE is_debit = 1
        GROUP BY merchant, category
        ORDER BY transaction_count DESC
        LIMIT 10
    """)

    run_query(conn, "3. Acquisition channel performance", """
        SELECT
            acquisition_channel,
            COUNT(DISTINCT user_id) AS total_users,
            COUNT(transaction_id) AS total_transactions,
            ROUND(SUM(amount), 2) AS total_spend,
            ROUND(SUM(amount) /
                COUNT(DISTINCT user_id), 2) AS spend_per_user
        FROM fct_transactions
        WHERE is_debit = 1
        GROUP BY acquisition_channel
        ORDER BY spend_per_user DESC
    """)

    run_query(conn, "4. Monthly spending trends", """
        SELECT
            transaction_month,
            COUNT(DISTINCT user_id) AS active_users,
            COUNT(transaction_id) AS total_transactions,
            ROUND(SUM(amount), 2) AS total_spend
        FROM fct_transactions
        WHERE is_debit = 1
        GROUP BY transaction_month
        ORDER BY transaction_month ASC
    """)

    run_query(conn, "5. Customer risk breakdown", """
        SELECT
            risk_segment,
            COUNT(user_id) AS total_users,
            ROUND(AVG(credit_score), 0) AS avg_credit_score,
            ROUND(AVG(balance), 2) AS avg_balance,
            ROUND(AVG(overdraft_count), 2) AS avg_overdrafts
        FROM dim_users
        GROUP BY risk_segment
        ORDER BY total_users DESC
    """)

    run_query(conn, "6. Spending by account type", """
        SELECT
            account_type,
            COUNT(DISTINCT user_id) AS total_users,
            ROUND(SUM(amount), 2) AS total_spend,
            ROUND(AVG(amount), 2) AS avg_transaction_amount,
            ROUND(SUM(amount) /
                COUNT(DISTINCT user_id), 2) AS spend_per_user
        FROM fct_transactions
        WHERE is_debit = 1
        GROUP BY account_type
        ORDER BY spend_per_user DESC
    """)

    conn.close()
    print("\nAnalysis complete.")

if __name__ == "__main__":
    main()