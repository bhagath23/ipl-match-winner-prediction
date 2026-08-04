import pandas as pd

matches = pd.read_csv("data/processed/matches_clean.csv")

matches = matches[matches["winner"] != "No Result"]

teams = pd.concat(
    [matches["team1"], matches["team2"]],
    ignore_index=True
).value_counts()

wins = matches["winner"].value_counts()

strength = pd.DataFrame({
    "Matches Played": teams,
    "Matches Won": wins
}).fillna(0)

strength["Matches Won"] = strength["Matches Won"].astype(int)

strength["Win Percentage"] = (
    strength["Matches Won"] /
    strength["Matches Played"] * 100
).round(2)

strength["Strength Rating"] = (
    strength["Win Percentage"] / 100
).round(3)

strength = strength.sort_values(
    by="Strength Rating",
    ascending=False
)

print("\nTeam Strength Ratings\n")
print(strength)