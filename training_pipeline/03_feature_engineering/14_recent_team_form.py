import pandas as pd

matches = pd.read_csv("data/processed/matches_clean.csv")

matches["date"] = pd.to_datetime(matches["date"])

matches = matches.sort_values(["date", "match_id"]).reset_index(drop=True)

team_history = {}

team1_recent_form = []
team2_recent_form = []

for _, row in matches.iterrows():

    team1 = row["team1"]
    team2 = row["team2"]
    winner = row["winner"]

    if team1 not in team_history:
        team_history[team1] = []

    if team2 not in team_history:
        team_history[team2] = []

    if len(team_history[team1]) == 0:
        team1_recent_form.append(0.5)
    else:
        last5 = team_history[team1][-5:]
        team1_recent_form.append(sum(last5) / len(last5))

    if len(team_history[team2]) == 0:
        team2_recent_form.append(0.5)
    else:
        last5 = team_history[team2][-5:]
        team2_recent_form.append(sum(last5) / len(last5))

    if winner == team1:
        team_history[team1].append(1)
        team_history[team2].append(0)
    elif winner == team2:
        team_history[team1].append(0)
        team_history[team2].append(1)

matches["team1_recent_form"] = team1_recent_form
matches["team2_recent_form"] = team2_recent_form

matches.to_csv(
    "data/processed/recent_form_feature.csv",
    index=False
)

print(
    matches[
        [
            "date",
            "team1",
            "team2",
            "team1_recent_form",
            "team2_recent_form",
            "winner"
        ]
    ].tail(20)
)

print("\nDataset Shape:", matches.shape)