import json
from pathlib import Path

# Path to the raw data folder
DATA_FOLDER = Path("data/raw")

first_file = sorted(DATA_FOLDER.glob("*.json"))[0]

print(f"Reading file: {first_file.name}")

with open(first_file, "r", encoding="utf-8") as file:
    match_data = json.load(file)

print("\nTop-level keys:")
print(match_data.keys())

info = match_data["info"]

print("\n" + "=" * 40)
print("MATCH DETAILS")
print("=" * 40)

print(f"Season          : {info['season']}")
print(f"Date            : {info['dates'][0]}")

print(f"Team 1          : {info['teams'][0]}")
print(f"Team 2          : {info['teams'][1]}")

print(f"Venue           : {info['venue']}")
print(f"City            : {info.get('city', 'N/A')}")

print(f"Overs           : {info['overs']}")

print(f"Toss Winner     : {info['toss']['winner']}")
print(f"Toss Decision   : {info['toss']['decision']}")

print(f"Winner          : {info['outcome']['winner']}")

print(f"Player of Match : {', '.join(info['player_of_match'])}")