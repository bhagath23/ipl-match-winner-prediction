import pandas as pd

matches = pd.read_csv("data/processed/matches_clean.csv")

matches["date"] = pd.to_datetime(matches["date"])

matches = matches.sort_values(
    ["date", "match_id"]
).reset_index(drop=True)

venue_history = {}

team1_venue_strength = []
team2_venue_strength = []

for _, row in matches.iterrows():

    team1 = row["team1"]
    team2 = row["team2"]
    venue = row["venue"]
    winner = row["winner"]

    key1 = (team1, venue)
    key2 = (team2, venue)

    if key1 not in venue_history:
        venue_history[key1] = {
            "played": 0,
            "won": 0
        }

    if key2 not in venue_history:
        venue_history[key2] = {
            "played": 0,
            "won": 0
        }

    if venue_history[key1]["played"] == 0:
        team1_venue_strength.append(0.5)
    else:
        team1_venue_strength.append(
            venue_history[key1]["won"] /
            venue_history[key1]["played"]
        )

    if venue_history[key2]["played"] == 0:
        team2_venue_strength.append(0.5)
    else:
        team2_venue_strength.append(
            venue_history[key2]["won"] /
            venue_history[key2]["played"]
        )

    venue_history[key1]["played"] += 1
    venue_history[key2]["played"] += 1

    if winner == team1:
        venue_history[key1]["won"] += 1

    elif winner == team2:
        venue_history[key2]["won"] += 1

matches["team1_venue_strength"] = team1_venue_strength
matches["team2_venue_strength"] = team2_venue_strength

matches.to_csv(
    "data/processed/venue_strength_feature.csv",
    index=False
)

print(
    matches[
        [
            "team1",
            "team2",
            "venue",
            "team1_venue_strength",
            "team2_venue_strength",
            "winner"
        ]
    ].tail(20)
)

print("\nShape:", matches.shape)