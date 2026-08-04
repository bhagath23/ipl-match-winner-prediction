import pandas as pd

from app.schemas.request import MatchRequest
from app.schemas.response import PredictionResponse
from app.service.model_loader import model, matches
from app.service.feature_engineering import (
    calculate_team_strength,
    calculate_recent_form,
    calculate_h2h,
    calculate_venue_strength,
)

VENUE_CITY = {
    "Arun Jaitley Stadium": "Delhi",
    "Barabati Stadium": "Cuttack",
    "Barsapara Cricket Stadium": "Guwahati",
    "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium": "Lucknow",
    "Brabourne Stadium": "Mumbai",
    "Buffalo Park": "East London",
    "De Beers Diamond Oval": "Kimberley",
    "Dr DY Patil Sports Academy": "Navi Mumbai",
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium": "Visakhapatnam",
    "Dubai International Cricket Stadium": "Dubai",
    "Eden Gardens": "Kolkata",
    "Green Park": "Kanpur",
    "Himachal Pradesh Cricket Association Stadium": "Dharamsala",
    "Holkar Cricket Stadium": "Indore",
    "JSCA International Stadium Complex": "Ranchi",
    "Kingsmead": "Durban",
    "M Chinnaswamy Stadium": "Bengaluru",
    "MA Chidambaram Stadium": "Chennai",
    "Maharaja Yadavindra Singh International Cricket Stadium": "New Chandigarh",
    "Maharashtra Cricket Association Stadium": "Pune",
    "Narendra Modi Stadium": "Ahmedabad",
    "Nehru Stadium": "Kochi",
    "New Wanderers Stadium": "Johannesburg",
    "Newlands": "Cape Town",
    "OUTsurance Oval": "Bloemfontein",
    "Punjab Cricket Association Stadium": "Mohali",
    "Rajiv Gandhi International Stadium": "Hyderabad",
    "Saurashtra Cricket Association Stadium": "Rajkot",
    "Sawai Mansingh Stadium": "Jaipur",
    "Shaheed Veer Narayan Singh International Stadium": "Raipur",
    "Sharjah Cricket Stadium": "Sharjah",
    "Sheikh Zayed Stadium": "Abu Dhabi",
    "St George's Park": "Port Elizabeth",
    "Subrata Roy Sahara Stadium": "Pune",
    "SuperSport Park": "Centurion",
    "Vidarbha Cricket Association Stadium": "Nagpur",
    "Wankhede Stadium": "Mumbai",
    "Zayed Cricket Stadium": "Abu Dhabi",
}


def predict_match(data: MatchRequest):

    city = VENUE_CITY.get(data.venue, "Unknown")

    team1_strength = calculate_team_strength(matches, data.team1)
    team2_strength = calculate_team_strength(matches, data.team2)

    team1_recent_form = calculate_recent_form(matches, data.team1)
    team2_recent_form = calculate_recent_form(matches, data.team2)

    team1_h2h, team2_h2h = calculate_h2h(
        matches,
        data.team1,
        data.team2,
    )

    team1_venue_strength = calculate_venue_strength(
        matches,
        data.team1,
        data.venue,
    )

    team2_venue_strength = calculate_venue_strength(
        matches,
        data.team2,
        data.venue,
    )

    input_df = pd.DataFrame(
        [
            {
                "team1": data.team1,
                "team2": data.team2,
                "venue": data.venue,
                "city": city,
                "toss_winner": data.toss_winner,
                "toss_decision": data.toss_decision,
                "team1_strength": team1_strength,
                "team2_strength": team2_strength,
                "team1_recent_form": team1_recent_form,
                "team2_recent_form": team2_recent_form,
                "team1_h2h": team1_h2h,
                "team2_h2h": team2_h2h,
                "team1_venue_strength": team1_venue_strength,
                "team2_venue_strength": team2_venue_strength,
            }
        ]
    )

    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    predicted_winner = data.team1 if prediction == 1 else data.team2

    return PredictionResponse(
        predicted_winner=predicted_winner,
        team1_probability=round(probabilities[1] * 100, 2),
        team2_probability=round(probabilities[0] * 100, 2),
        team1_strength=round(team1_strength, 3),
        team2_strength=round(team2_strength, 3),
        team1_recent_form=round(team1_recent_form, 3),
        team2_recent_form=round(team2_recent_form, 3),
        team1_h2h=round(team1_h2h, 3),
        team2_h2h=round(team2_h2h, 3),
        team1_venue_strength=round(team1_venue_strength, 3),
        team2_venue_strength=round(team2_venue_strength, 3),
    )