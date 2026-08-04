from pydantic import BaseModel


class PredictionResponse(BaseModel):
    predicted_winner: str
    team1_probability: float
    team2_probability: float

    team1_strength: float
    team2_strength: float

    team1_recent_form: float
    team2_recent_form: float

    team1_h2h: float
    team2_h2h: float

    team1_venue_strength: float
    team2_venue_strength: float