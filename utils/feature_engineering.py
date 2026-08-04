import pandas as pd


def get_team_strength(team, matches):
    team_matches = matches[
        (matches["team1"] == team) | (matches["team2"] == team)
    ]

    total_matches = len(team_matches)

    if total_matches == 0:
        return 0.5

    wins = (team_matches["winner"] == team).sum()

    return (wins + 1) / (total_matches + 2)


def get_recent_form(team, matches, last_n=5):
    team_matches = matches[
        (matches["team1"] == team) | (matches["team2"] == team)
    ].tail(last_n)

    total_matches = len(team_matches)

    if total_matches == 0:
        return 0.5

    wins = (team_matches["winner"] == team).sum()

    return (wins + 1) / (total_matches + 2)


def get_head_to_head(team1, team2, matches):
    h2h = matches[
        (
            ((matches["team1"] == team1) & (matches["team2"] == team2))
            |
            ((matches["team1"] == team2) & (matches["team2"] == team1))
        )
    ]

    total_matches = len(h2h)

    if total_matches == 0:
        return 0.5, 0.5

    team1_wins = (h2h["winner"] == team1).sum()
    team2_wins = (h2h["winner"] == team2).sum()

    team1_strength = (team1_wins + 1) / (total_matches + 2)
    team2_strength = (team2_wins + 1) / (total_matches + 2)

    return team1_strength, team2_strength


def get_venue_strength(team, venue, matches):
    venue_matches = matches[
        (
            ((matches["team1"] == team) | (matches["team2"] == team))
            &
            (matches["venue"] == venue)
        )
    ]

    total_matches = len(venue_matches)

    if total_matches == 0:
        return 0.5

    wins = (venue_matches["winner"] == team).sum()

    return (wins + 1) / (total_matches + 2)


def create_feature_dict(
    team1,
    team2,
    venue,
    city,
    toss_winner,
    toss_decision,
    matches,
):
    team1_strength = get_team_strength(team1, matches)
    team2_strength = get_team_strength(team2, matches)

    team1_recent_form = get_recent_form(team1, matches)
    team2_recent_form = get_recent_form(team2, matches)

    team1_h2h, team2_h2h = get_head_to_head(
        team1,
        team2,
        matches,
    )

    team1_venue_strength = get_venue_strength(
        team1,
        venue,
        matches,
    )

    team2_venue_strength = get_venue_strength(
        team2,
        venue,
        matches,
    )

    features = pd.DataFrame(
        [{
            "team1": team1,
            "team2": team2,
            "venue": venue,
            "city": city,
            "toss_winner": toss_winner,
            "toss_decision": toss_decision,
            "team1_strength": team1_strength,
            "team2_strength": team2_strength,
            "team1_recent_form": team1_recent_form,
            "team2_recent_form": team2_recent_form,
            "team1_h2h": team1_h2h,
            "team2_h2h": team2_h2h,
            "team1_venue_strength": team1_venue_strength,
            "team2_venue_strength": team2_venue_strength,
        }]
    )

    return features