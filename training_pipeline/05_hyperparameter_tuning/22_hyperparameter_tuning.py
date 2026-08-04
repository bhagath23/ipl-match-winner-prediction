from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "processed" / "ml_dataset.csv"

MODEL_DIR = BASE_DIR / "models"
ARTIFACT_DIR = BASE_DIR / "artifacts"

MODEL_DIR.mkdir(exist_ok=True)
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

categorical_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent"),
        ),
        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore"),
        ),
    ]
)

numerical_transformer = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median"),
        )
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            categorical_transformer,
            categorical_features,
        ),
        (
            "numerical",
            numerical_transformer,
            numerical_features,
        ),
    ]
)

pipeline = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor,
        ),
        (
            "classifier",
            DecisionTreeClassifier(random_state=42),
        ),
    ]
)

param_grid = {
    "classifier__criterion": [
        "gini",
        "entropy",
    ],
    "classifier__max_depth": [
        5,
        10,
        15,
        None,
    ],
    "classifier__min_samples_split": [
        2,
        5,
        10,
    ],
    "classifier__min_samples_leaf": [
        1,
        2,
        4,
    ],
    "classifier__ccp_alpha": [
        0.0,
        0.001,
    ],
}

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1,
    verbose=1,
)

print("=" * 70)
print("Starting Hyperparameter Tuning...")
print("=" * 70)

grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print()

print("=" * 70)
print("Best Hyperparameters")
print("=" * 70)
print(grid_search.best_params_)

print()

print(f"Best Cross Validation Accuracy : {grid_search.best_score_:.4f}")
print(f"Test Accuracy                  : {accuracy:.4f}")

print()

print("=" * 70)
print("Classification Report")
print("=" * 70)
print(classification_report(y_test, y_pred))

joblib.dump(
    best_model,
    MODEL_DIR / "best_model.pkl",
)

joblib.dump(
    best_model.named_steps["preprocessor"],
    ARTIFACT_DIR / "preprocessor.pkl",
)

print()

print("=" * 70)
print("Model Saved Successfully")
print("=" * 70)
print("Model        :", MODEL_DIR / "best_model.pkl")
print("Preprocessor :", ARTIFACT_DIR / "preprocessor.pkl")
print("=" * 70)