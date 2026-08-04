from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "processed" / "ml_dataset.csv"

ARTIFACT_DIR = BASE_DIR / "artifacts"
ARTIFACT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

df = df[df["winner"] != "No Result"].copy()

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date").reset_index(drop=True)

df["target"] = (df["winner"] == df["team1"]).astype(int)

split_index = int(len(df) * 0.80)

train_df = df.iloc[:split_index].copy()
test_df = df.iloc[split_index:].copy()

X_train = train_df.drop(
    columns=[
        "match_id",
        "date",
        "season",
        "winner",
        "target",
    ]
)

X_test = test_df.drop(
    columns=[
        "match_id",
        "date",
        "season",
        "winner",
        "target",
    ]
)

y_train = train_df["target"]
y_test = test_df["target"]

joblib.dump(X_train, ARTIFACT_DIR / "X_train_catboost.pkl")
joblib.dump(X_test, ARTIFACT_DIR / "X_test_catboost.pkl")
joblib.dump(y_train, ARTIFACT_DIR / "y_train_catboost.pkl")
joblib.dump(y_test, ARTIFACT_DIR / "y_test_catboost.pkl")

print("=" * 70)
print("CATBOOST DATA PREP COMPLETED")
print("=" * 70)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

print()
print("Artifacts Saved Successfully")