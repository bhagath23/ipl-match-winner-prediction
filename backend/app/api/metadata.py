from fastapi import APIRouter
import pandas as pd
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "matches_clean.csv"

df = pd.read_csv(DATA_PATH)

CURRENT_TEAMS = [
    "Chennai Super Kings",
    "Delhi Capitals",
    "Gujarat Titans",
    "Kolkata Knight Riders",
    "Lucknow Super Giants",
    "Mumbai Indians",
    "Punjab Kings",
    "Rajasthan Royals",
    "Royal Challengers Bengaluru",
    "Sunrisers Hyderabad",
]

teams = CURRENT_TEAMS

venues = sorted(df["venue"].dropna().unique().tolist())


@router.get("/metadata")
def get_metadata():
    return {
        "teams": teams,
        "venues": venues,
    }