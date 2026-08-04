from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

PROCESSED_DIR = BASE_DIR / "data" / "processed"

matches = pd.read_csv(PROCESSED_DIR / "matches_clean.csv")

strength = pd.read_csv(PROCESSED_DIR / "historical_team_strength.csv")
recent = pd.read_csv(PROCESSED_DIR / "recent_form_feature.csv")
h2h = pd.read_csv(PROCESSED_DIR / "head_to_head_feature.csv")
venue = pd.read_csv(PROCESSED_DIR / "venue_strength_feature.csv")

ml = matches.copy()

ml = ml.merge(
    strength[
        [
            "match_id",
            "team1_strength",
            "team2_strength"
        ]
    ],
    on="match_id",
    how="left"
)

ml = ml.merge(
    recent[
        [
            "match_id",
            "team1_recent_form",
            "team2_recent_form"
        ]
    ],
    on="match_id",
    how="left"
)

ml = ml.merge(
    h2h[
        [
            "match_id",
            "team1_h2h",
            "team2_h2h"
        ]
    ],
    on="match_id",
    how="left"
)

ml = ml.merge(
    venue[
        [
            "match_id",
            "team1_venue_strength",
            "team2_venue_strength"
        ]
    ],
    on="match_id",
    how="left"
)

ml = ml[
    [
        "match_id",
        "date",
        "season",
        "team1",
        "team2",
        "venue",
        "city",
        "toss_winner",
        "toss_decision",
        "team1_strength",
        "team2_strength",
        "team1_recent_form",
        "team2_recent_form",
        "team1_h2h",
        "team2_h2h",
        "team1_venue_strength",
        "team2_venue_strength",
        "winner",
    ]
]

ml["date"] = pd.to_datetime(ml["date"])

ml = (
    ml.sort_values(
        ["date", "match_id"]
    )
    .reset_index(drop=True)
)

print("=" * 70)
print("ML Dataset Shape :", ml.shape)
print("=" * 70)

print(ml.head())

ml.to_csv(
    PROCESSED_DIR / "ml_dataset.csv",
    index=False
)

print("\nSaved to:", PROCESSED_DIR / "ml_dataset.csv")