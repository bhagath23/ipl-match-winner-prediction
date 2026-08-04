from pathlib import Path

import joblib

BASE_DIR = Path(__file__).resolve().parents[2].parents[0]

X_train = joblib.load(BASE_DIR / "artifacts" / "X_train_catboost.pkl")

print(X_train.columns.tolist())