import pandas as pd
from pathlib import Path


MATCHES_FILE = Path("data/processed/matches.csv")
DELIVERIES_FILE = Path("data/processed/deliveries.csv")

OUTPUT_MATCHES = Path("data/processed/matches_clean.csv")
OUTPUT_DELIVERIES = Path("data/processed/deliveries_clean.csv")


matches = pd.read_csv(MATCHES_FILE)
deliveries = pd.read_csv(DELIVERIES_FILE)

print("=" * 60)
print("BEFORE CLEANING")
print("=" * 60)

print(f"Matches Shape    : {matches.shape}")
print(f"Deliveries Shape : {deliveries.shape}")



matches["city"] = matches["city"].fillna("Unknown")
matches["player_of_match"] = matches["player_of_match"].fillna("No Award")



deliveries = deliveries.drop_duplicates()

deliveries["dismissal_type"] = deliveries["dismissal_type"].fillna("Not Out")
deliveries["player_out"] = deliveries["player_out"].fillna("Not Applicable")



matches.to_csv(OUTPUT_MATCHES, index=False)
deliveries.to_csv(OUTPUT_DELIVERIES, index=False)

print("\n" + "=" * 60)
print("AFTER CLEANING")
print("=" * 60)

print(f"Matches Shape    : {matches.shape}")
print(f"Deliveries Shape : {deliveries.shape}")

print("\nFiles Saved Successfully")
print(OUTPUT_MATCHES)
print(OUTPUT_DELIVERIES)