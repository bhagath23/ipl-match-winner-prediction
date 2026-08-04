import pandas as pd

matches = pd.read_csv("data/processed/matches_clean.csv")

matches["date"] = pd.to_datetime(matches["date"])

matches = matches.sort_values(["date", "match_id"]).reset_index(drop=True)

head_to_head = {}

team1_h2h = []
team2_h2h = []

for _, row in matches.iterrows():

    team1 = row["team1"]
    team2 = row["team2"]
    winner = row["winner"]

    pair = tuple(sorted([team1, team2]))

    if pair not in head_to_head:
        head_to_head[pair] = {
            team1: 0,
            team2: 0
        }

    if team1 not in head_to_head[pair]:
        head_to_head[pair][team1] = 0

    if team2 not in head_to_head[pair]:
        head_to_head[pair][team2] = 0

    total_matches = (
        head_to_head[pair][team1] +
        head_to_head[pair][team2]
    )

    if total_matches == 0:
        team1_h2h.append(0.5)
        team2_h2h.append(0.5)
    else:
        team1_h2h.append(
            head_to_head[pair][team1] / total_matches
        )
        team2_h2h.append(
            head_to_head[pair][team2] / total_matches
        )

    if winner == team1:
        head_to_head[pair][team1] += 1
    elif winner == team2:
        head_to_head[pair][team2] += 1

matches["team1_h2h"] = team1_h2h
matches["team2_h2h"] = team2_h2h

matches.to_csv(
    "data/processed/head_to_head_feature.csv",
    index=False
)

print(
    matches[
        [
            "team1",
            "team2",
            "team1_h2h",
            "team2_h2h",
            "winner"
        ]
    ].tail(20)
)

print("\nShape:", matches.shape)