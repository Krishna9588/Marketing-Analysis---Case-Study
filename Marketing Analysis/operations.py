import pandas as pd

# Load Data set
p_df = pd.read_csv("dataset/purchase_behaviour.csv")
t_df = pd.read_csv("dataset/transaction_data.csv")

# Merge datasets = m_df file
# Using LYLTY_CARD_NBR (Customer ID) as Primary key and Foreign key
m_df = t_df.merge(p_df, on="LYLTY_CARD_NBR")

# To get merged file as .csv use this command
# m_df.to_csv("dataset/merged_new.csv")
