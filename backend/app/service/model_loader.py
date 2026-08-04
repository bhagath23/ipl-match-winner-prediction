from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models" / "catboost_model.pkl"
DATA_PATH = BASE_DIR / "data" / "matches_clean.csv"

model = joblib.load(MODEL_PATH)

matches = pd.read_csv(DATA_PATH)


team_mapping = {
    "Delhi Daredevils": "Delhi Capitals",
    "Kings XI Punjab": "Punjab Kings",
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
}

for column in ["team1", "team2", "winner"]:
    if column in matches.columns:
        matches[column] = matches[column].replace(team_mapping)



venue_mapping = {
    "M Chinnaswamy Stadium, Bengaluru": "M Chinnaswamy Stadium",
    "M.Chinnaswamy Stadium": "M Chinnaswamy Stadium",

    "MA Chidambaram Stadium, Chepauk": "MA Chidambaram Stadium",
    "M. A. Chidambaram Stadium": "MA Chidambaram Stadium",

    "Feroz Shah Kotla": "Arun Jaitley Stadium",

    "Punjab Cricket Association IS Bindra Stadium": "Punjab Cricket Association Stadium",
    "Punjab Cricket Association IS Bindra Stadium, Mohali": "Punjab Cricket Association Stadium",

    "Rajiv Gandhi International Stadium, Uppal": "Rajiv Gandhi International Stadium",

    "Sardar Patel Stadium, Motera": "Narendra Modi Stadium",

    "BRSABV Ekana Cricket Stadium": "Ekana Cricket Stadium",
}

if "venue" in matches.columns:
    matches["venue"] = matches["venue"].replace(venue_mapping)



matches["date"] = pd.to_datetime(matches["date"])
matches = matches.sort_values(["date", "match_id"]).reset_index(drop=True)