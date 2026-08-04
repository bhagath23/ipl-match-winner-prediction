import pandas as pd

matches = pd.read_csv("data/processed/matches_clean.csv")

team_name_mapping = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Rising Pune Supergiants": "Rising Pune Supergiant",
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru"
}

columns = ["team1", "team2", "winner", "toss_winner"]

for column in columns:
    matches[column] = matches[column].replace(team_name_mapping)

matches.to_csv("data/processed/matches_clean.csv", index=False)

print("Team names standardized successfully.")