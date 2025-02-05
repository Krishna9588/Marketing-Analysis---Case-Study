import pandas as pd
from operations import *

# Identifying top 10% customer - Most Frequent and High-Spending Customers
top_f = m_df["LYLTY_CARD_NBR"].value_counts().quantile(0.90)
top_s = m_df.groupby("LYLTY_CARD_NBR")["TOT_SALES"].sum().quantile(0.90)

print(f"Minimum number of transactions to be in top 10% = {top_f}")
print(f"Minimum total spending a customer must have to be in top 10% = {top_s} ")

loyal_c = m_df.groupby("LYLTY_CARD_NBR").filter(
    lambda x: len(x) > top_f or x["TOT_SALES"].sum() > top_s
)

# Now we have Top 10% audience here is there characteristics
loyal_c = (
    loyal_c.groupby(["LYLTY_CARD_NBR", "LIFESTAGE", "PREMIUM_CUSTOMER"])
    .agg(TRANSACTION_COUNT=("TXN_ID", "count"),
         TOTAL_SPENT=("TOT_SALES", "sum"))
    .reset_index()
)

x = int(input("\nEnter number for top most loyal customers : "))

# Get Top x Loyal Customers (Sorted by Transactions, then Spending)

top_x_loyal_c = loyal_c.sort_values(
    ["TRANSACTION_COUNT", "TOTAL_SPENT"], ascending=[False, False]
).head(x)

# Save to dataset folder
top_x_loyal_c.to_csv(f"dataset/top_{x}_loyal_customers.csv", index=False)

print(f"\nTop {x} loyal customer insights saved to 'top_{x}_loyal_customers.csv'")

print(top_x_loyal_c[0:5])  # Display (top) first 5 customers