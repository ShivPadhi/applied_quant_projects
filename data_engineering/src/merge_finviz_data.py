import pandas as pd

# Load our datasets (I omitted the name of our dataset so it is customizable here)
tickers_df = pd.read_csv("dataset.csv")  # Columns: Date, day_of_week, Ticker for example

#This is from a extracted csv of finviz data correlating to the tickers we picked for our dataset
finviz_df = pd.read_csv("finvizdata.csv")  # Columns: Ticker, Company, Sector, Industry

# Clean column names (remove leading/trailing spaces)

tickers_df.rename(columns=str.strip, inplace=True)
finviz_df.rename(columns=str.strip, inplace=True)

# Merge Finviz data into dataset on 'Ticker' column

merged_df = tickers_df.merge(
    finviz_df,
    on="Ticker",
    how="left"  # keep all rows from tickers_df, add matching Finviz info
)

# Reorder columns to a desired order. For example: Date, day_of_week, Ticker, Company, Sector, Industry

desired_order = ["Date", "day_of_week", "Ticker", "Company", "Sector", "Industry"]
merged_df = merged_df[desired_order]

# Save merged dataset to CSV
merged_df.to_csv("tickers_with_finviz.csv", index=False)

# Print sample output
print(merged_df.head())
