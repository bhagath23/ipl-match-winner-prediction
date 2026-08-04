import json
from pathlib import Path
import pandas as pd


RAW_DATA = Path("data/raw")
OUTPUT_FILE = Path("data/processed/deliveries.csv")

deliveries = []


for file_path in sorted(RAW_DATA.glob("*.json")):

    match_id = file_path.stem

    with open(file_path, "r", encoding="utf-8") as f:
        match = json.load(f)

    for innings_number, innings in enumerate(match["innings"], start=1):

        batting_team = innings["team"]

        for over in innings["overs"]:

            over_number = over["over"]

            for delivery in over["deliveries"]:

                is_wicket = "wickets" in delivery

                dismissal_type = None
                player_out = None

                if is_wicket:
                    dismissal_type = delivery["wickets"][0].get("kind")
                    player_out = delivery["wickets"][0].get("player_out")

                deliveries.append({

                    "match_id": match_id,
                    "innings": innings_number,
                    "batting_team": batting_team,

                    "over": over_number,
                    "ball": delivery["actual_delivery"],

                    "batter": delivery["batter"],
                    "bowler": delivery["bowler"],
                    "non_striker": delivery["non_striker"],

                    "batsman_runs": delivery["runs"]["batter"],
                    "extras": delivery["runs"]["extras"],
                    "total_runs": delivery["runs"]["total"],

                    "is_four": delivery["runs"]["batter"] == 4,
                    "is_six": delivery["runs"]["batter"] == 6,

                    "is_wicket": is_wicket,
                    "dismissal_type": dismissal_type,
                    "player_out": player_out
                })


deliveries_df = pd.DataFrame(deliveries)

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

deliveries_df.to_csv(OUTPUT_FILE, index=False)

print("=" * 50)
print("DELIVERIES EXTRACTION COMPLETED")
print("=" * 50)

print(f"Total Deliveries : {len(deliveries_df)}")
print(f"Saved To         : {OUTPUT_FILE}")

print("\nColumns:")
print(deliveries_df.columns.tolist())

print("\nFirst 5 Rows:")
print(deliveries_df.head())