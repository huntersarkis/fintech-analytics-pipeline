import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta

# Configuration
random.seed(42)
np.random.seed(42)

NUM_USERS = 500
NUM_TRANSACTIONS = 10000
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2024, 12, 31)

# Reference data
CATEGORIES = ["Food & Dining", "Shopping", "Travel", "Entertainment",
              "Healthcare", "Utilities", "Income", "Transfer"]

MERCHANTS = {
    "Food & Dining": ["Starbucks", "McDonalds", "Chipotle", "DoorDash", "Uber Eats"],
    "Shopping": ["Amazon", "Target", "Walmart", "Nike", "Apple Store"],
    "Travel": ["Delta Airlines", "Airbnb", "Uber", "Lyft", "Marriott"],
    "Entertainment": ["Netflix", "Spotify", "Steam", "AMC Theatres", "ESPN+"],
    "Healthcare": ["CVS Pharmacy", "Walgreens", "ZocDoc", "One Medical", "Cigna"],
    "Utilities": ["Comcast", "AT&T", "Con Edison", "National Grid", "T-Mobile"],
    "Income": ["Employer Direct Deposit", "Freelance Payment", "Venmo Transfer"],
    "Transfer": ["Venmo", "PayPal", "Zelle", "Cash App", "Bank Transfer"]
}

ACQUISITION_CHANNELS = ["organic", "referral", "paid_social", "paid_search", "influencer"]
ACCOUNT_TYPES = ["checking", "savings", "premium"]
US_STATES = ["CA", "NY", "TX", "FL", "WA", "IL", "MA", "CO", "GA", "AZ"]

# Generate users
def generate_users(n):
    users = []
    for i in range(1, n + 1):
        signup_date = START_DATE + timedelta(days=random.randint(0, 365))
        users.append({
            "user_id": f"U{i:04d}",
            "name": f"User {i}",
            "email": f"user{i}@example.com",
            "state": random.choice(US_STATES),
            "account_type": random.choice(ACCOUNT_TYPES),
            "acquisition_channel": random.choice(ACQUISITION_CHANNELS),
            "signup_date": signup_date.strftime("%Y-%m-%d"),
            "is_active": random.choices([1, 0], weights=[85, 15])[0]
        })
    return pd.DataFrame(users)

#  Generate transactions
def generate_transactions(users_df, n):
    transactions = []
    for i in range(1, n + 1):
        user = users_df.sample(1).iloc[0]
        category = random.choice(CATEGORIES)
        merchant = random.choice(MERCHANTS[category])
        date = START_DATE + timedelta(days=random.randint(0, 729))

        if category == "Income":
            amount = round(random.uniform(1000, 8000), 2)
        elif category == "Transfer":
            amount = round(random.uniform(20, 2000), 2)
        else:
            amount = round(random.uniform(2, 500), 2)

        transactions.append({
            "transaction_id": f"T{i:06d}",
            "user_id": user["user_id"],
            "date": date.strftime("%Y-%m-%d"),
            "merchant": merchant,
            "category": category,
            "amount": amount,
            "is_debit": 0 if category == "Income" else 1,
            "status": random.choices(["completed", "pending", "failed"],
                                     weights=[90, 7, 3])[0]
        })
    return pd.DataFrame(transactions)

# Generate account balances
def generate_balances(users_df):
    balances = []
    for _, user in users_df.iterrows():
        balances.append({
            "user_id": user["user_id"],
            "account_type": user["account_type"],
            "balance": round(random.uniform(100, 50000), 2),
            "credit_score": random.randint(580, 850),
            "overdraft_count": random.choices([0, 1, 2, 3], weights=[70, 15, 10, 5])[0],
            "snapshot_date": END_DATE.strftime("%Y-%m-%d")
        })
    return pd.DataFrame(balances)

# Save to CSV
def main():
    os.makedirs("data/raw", exist_ok=True)

    print("Generating users...")
    users_df = generate_users(NUM_USERS)
    users_df.to_csv("data/raw/users.csv", index=False)
    print(f"  {len(users_df)} users saved to data/raw/users.csv")

    print("Generating transactions...")
    transactions_df = generate_transactions(users_df, NUM_TRANSACTIONS)
    transactions_df.to_csv("data/raw/transactions.csv", index=False)
    print(f"  {len(transactions_df)} transactions saved to data/raw/transactions.csv")

    print("Generating account balances...")
    balances_df = generate_balances(users_df)
    balances_df.to_csv("data/raw/account_balances.csv", index=False)
    print(f"  {len(balances_df)} balances saved to data/raw/account_balances.csv")

    print("\nAll raw data generated successfully.")

if __name__ == "__main__":
    main()