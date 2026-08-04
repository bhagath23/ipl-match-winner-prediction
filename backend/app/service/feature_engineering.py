import pandas as pd


def calculate_team_strength(matches, team):
    team_matches = matches[
        (matches["team1"] == team) | (matches["team2"] == team)
    ]

    matches_played = len(team_matches)

    if matches_played == 0:
        return 0.5

    matches_won = (team_matches["winner"] == team).sum()

    return matches_won / matches_played


def calculate_recent_form(matches, team, last_n=5):
    team_matches = matches[
        (matches["team1"] == team) | (matches["team2"] == team)
    ]

    team_matches = team_matches.sort_values("date")

    if len(team_matches) == 0:
        return 0.5

    recent = team_matches.tail(last_n)

    wins = (recent["winner"] == team).sum()

    return wins / len(recent)


def calculate_h2h(matches, team1, team2):
    h2h = matches[
        (
            (matches["team1"] == team1)
            & (matches["team2"] == team2)
        )
        |
        (
            (matches["team1"] == team2)
            & (matches["team2"] == team1)
        )
    ]

    if len(h2h) == 0:
        return 0.5, 0.5

    team1_wins = (h2h["winner"] == team1).sum()
    team2_wins = (h2h["winner"] == team2).sum()

    total = team1_wins + team2_wins

    if total == 0:
        return 0.5, 0.5

    return (
        team1_wins / total,
        team2_wins / total,
    )


def calculate_venue_strength(matches, team, venue):
    venue_matches = matches[
        (
            (matches["team1"] == team)
            | (matches["team2"] == team)
        )
        &
        (matches["venue"] == venue)
    ]

    if len(venue_matches) == 0:
        return 0.5

    wins = (venue_matches["winner"] == team).sum()

    return wins / len(venue_matches)