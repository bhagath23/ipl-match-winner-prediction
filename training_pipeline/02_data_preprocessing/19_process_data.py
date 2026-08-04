from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


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

categorical_features = [
    "team1",
    "team2",
    "venue",
    "city",
    "toss_winner",
    "toss_decision",
]

numerical_features = [
    "team1_strength",
    "team2_strength",
    "team1_recent_form",
    "team2_recent_form",
    "team1_h2h",
    "team2_h2h",
    "team1_venue_strength",
    "team2_venue_strength",
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features,
        ),
        (
            "numerical",
            "passthrough",
            numerical_features,
        ),
    ]
)

preprocessor.fit(X_train)

X_train_processed = preprocessor.transform(X_train)
X_test_processed = preprocessor.transform(X_test)

joblib.dump(preprocessor, ARTIFACT_DIR / "preprocessor.pkl")
joblib.dump(X_train_processed, ARTIFACT_DIR / "X_train.pkl")
joblib.dump(X_test_processed, ARTIFACT_DIR / "X_test.pkl")
joblib.dump(y_train, ARTIFACT_DIR / "y_train.pkl")
joblib.dump(y_test, ARTIFACT_DIR / "y_test.pkl")

print("=" * 70)
print("PREPROCESSING COMPLETED")
print("=" * 70)

print(f"Total Matches      : {len(df)}")
print(f"Training Samples   : {len(train_df)}")
print(f"Testing Samples    : {len(test_df)}")

print()

print(
    f"Training Dates : {train_df['date'].min().date()} ---> {train_df['date'].max().date()}"
)

print(
    f"Testing Dates  : {test_df['date'].min().date()} ---> {test_df['date'].max().date()}"
)

print()

print("Training Seasons")
print(sorted(train_df["season"].unique()))

print()

print("Testing Seasons")
print(sorted(test_df["season"].unique()))

print()

print(f"Encoded Train Shape : {X_train_processed.shape}")
print(f"Encoded Test Shape  : {X_test_processed.shape}")

print()

print("Artifacts Saved Successfully")