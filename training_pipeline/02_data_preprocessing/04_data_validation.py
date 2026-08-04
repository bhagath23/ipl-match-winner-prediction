import pandas as pd
from pathlib import Path


MATCHES_FILE = Path("data/processed/matches.csv")
DELIVERIES_FILE = Path("data/processed/deliveries.csv")


matches = pd.read_csv(MATCHES_FILE)
deliveries = pd.read_csv(DELIVERIES_FILE)


def analyze_dataset(df, name):

    print("\n" + "=" * 60)
    print(f"{name.upper()} DATASET")
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())


analyze_dataset(matches, "Matches")

analyze_dataset(deliveries, "Deliveries")