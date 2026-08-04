from pathlib import Path

import joblib

from catboost import CatBoostClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
)

BASE_DIR = Path(__file__).resolve().parents[1]

ARTIFACT_DIR = BASE_DIR / "artifacts"
MODEL_DIR = BASE_DIR / "models"

MODEL_DIR.mkdir(exist_ok=True)

X_train = joblib.load(ARTIFACT_DIR / "X_train.pkl")
X_test = joblib.load(ARTIFACT_DIR / "X_test.pkl")
y_train = joblib.load(ARTIFACT_DIR / "y_train.pkl")
y_test = joblib.load(ARTIFACT_DIR / "y_test.pkl")

model = CatBoostClassifier(
    iterations=500,
    learning_rate=0.05,
    depth=8,
    loss_function="Logloss",
    eval_metric="AUC",
    random_seed=42,
    verbose=100,
)

print("=" * 70)
print("TRAINING CATBOOST MODEL")
print("=" * 70)

model.fit(X_train, y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)
roc_auc = roc_auc_score(y_test, probabilities)

cm = confusion_matrix(y_test, predictions)

joblib.dump(model, MODEL_DIR / "catboost_model.pkl")

print()
print("=" * 70)
print("CATBOOST RESULTS")
print("=" * 70)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"ROC-AUC   : {roc_auc:.4f}")

print()
print("=" * 70)
print("CONFUSION MATRIX")
print("=" * 70)

print(cm)

print()
print("=" * 70)
print("MODEL SAVED")
print("=" * 70)

print(MODEL_DIR / "catboost_model.pkl")