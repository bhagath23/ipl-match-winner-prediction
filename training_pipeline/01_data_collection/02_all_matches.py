import json
from pathlib import Path

import pandas as pd

RAW_DATA = Path("data/raw")
OUTPUT_FILE = Path("data/processed/matches.csv")

matches = []

for file_path in sorted(RAW_DATA.glob("*.json")):

    with open(file_path, "r", encoding="utf-8") as file:
        match = json.load(file)

    info = match["info"]

    match_record = {
        "match_id": file_path.stem,
        "season": info["season"],
        "date": info["dates"][0],
        "team1": info["teams"][0],
        "team2": info["teams"][1],
        "venue": info["venue"],
        "city": info.get("city", "N/A"),
        "overs": info["overs"],
        "toss_winner": info["toss"]["winner"],
        "toss_decision": info["toss"]["decision"],
        "winner": info["outcome"].get("winner", "No Result"),
        "player_of_match": ", ".join(info.get("player_of_match", []))
    }

    matches.append(match_record)

matches_df = pd.DataFrame(matches)

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

matches_df.to_csv(OUTPUT_FILE, index=False)

print("=" * 40)
print("MATCH DATA EXTRACTION COMPLETED")
print("=" * 40)
print(f"Total Matches : {len(matches_df)}")
print(f"Saved To      : {OUTPUT_FILE}")

print("\nFirst 5 Matches:")
print(matches_df.head())