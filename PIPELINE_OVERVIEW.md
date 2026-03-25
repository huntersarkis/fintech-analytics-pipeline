# Fintech Analytics Pipeline — Project Overview

## What This Project Simulates

This project simulates the data infrastructure of a fintech application — similar to a personal finance tool like Mint or a neobank like Chime. The pipeline ingests raw user, transaction, and account data and transforms it into clean, analytics-ready models that support business decision-making.

This mirrors the day-to-day work of an analytics engineering team: taking messy raw data and building reliable, maintainable pipelines that the rest of the business can trust and query.

---

## The Data

The pipeline is built on three core datasets generated to simulate real-world fintech data:

**Users** — 500 customers with attributes including account type (checking, savings, premium), acquisition channel (organic, referral, paid social, paid search, influencer), state, and signup date.

**Transactions** — 10,000 financial transactions across two years (2023–2024) covering categories including Food & Dining, Shopping, Travel, Entertainment, Healthcare, Utilities, Income, and Transfers. Each transaction includes merchant, amount, date, and status.

**Account Balances** — a snapshot of each user's financial health including current balance, credit score, and overdraft history.

---

## Pipeline Architecture

The pipeline is structured in three layers, following analytics engineering best practices:

### Staging Layer
The staging layer takes each raw table and applies cleaning and standardization — handling nulls, standardizing date formats, renaming columns for consistency, and filtering out failed transactions. No raw table is ever queried directly by downstream models. This ensures every model built on top of staging is working with clean, reliable data.

### Mart Layer
The mart layer joins and aggregates staged data into fact and dimension tables ready for business analysis. Fact tables capture measurable events (transactions, revenue). Dimension tables capture descriptive attributes (user profiles). This structure mirrors production data modeling patterns used by analytics engineering teams at real companies.

### Metrics Layer
The metrics layer calculates the KPIs the business actually cares about — monthly spending by category, top merchants by volume, acquisition channel performance, and customer risk indicators based on credit score and overdraft behavior.

---

## Tech Stack

- Python (pandas) — data generation and ingestion
- SQL — data modeling and transformation
- SQLite — local data warehouse
- Git & GitHub — version control

---

## Key Business Insights

- Identified top spending categories and merchants driving transaction volume
- Analyzed acquisition channel performance to surface which channels bring the highest value users
- Built a customer risk model flagging users with high overdraft counts and low credit scores
- Modeled monthly revenue trends across user segments and account types

---

## Project Structure
```
fintech-analytics-pipeline/
│
├── data/
│   └── raw/
│       ├── users.csv
│       ├── transactions.csv
│       └── account_balances.csv
│
├── sql/
│   ├── staging/
│   ├── marts/
│   └── analysis/
│
├── python/
│   ├── generate_data.py
│   └── load_to_sqlite.py
│
├── notebooks/
├── fintech_analytics.db
├── PIPELINE_OVERVIEW.md
└── README.md
```

---

## Author

Hunter Sarkis
Grand Canyon University — M.S. in Business Analytics
Analytics Engineer