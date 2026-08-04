import pandas as pd
from pathlib import Path

DELIVERIES = Path("data/processed/deliveries.csv")

df = pd.read_csv(DELIVERIES)

duplicates = df[df.duplicated(keep=False)]

print("=" * 60)
print("TOTAL DUPLICATE ROWS")
print("=" * 60)

print(len(duplicates))

print("\nFirst 20 Duplicate Rows:")
print(duplicates.head(20))