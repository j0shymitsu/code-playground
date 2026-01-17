import random

win_points = 3
draw_points = 1
lose_points = 0

teams = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton & Hove Albion",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Ipswich Town",
    "Leicester City",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Southampton",
    "Tottenham Hotspur",
    "West Ham United",
    "Wolverhampton Wanderers"
]

league_table = {team: 0 for team in teams}

fixtures = []

for home in teams:
    for away in teams:
        if home != away: 
            fixtures.append((home, away))

for home, away in fixtures:
    result = random.choice(["home_win", "away_win", "draw"])

    if result == "home_win":
        league_table[home] += win_points
        league_table[away] += lose_points
    elif result == "away_win":
        league_table[home] += lose_points
        league_table[away] += win_points
    else:    # draw result
        league_table[home] += draw_points
        league_table[away] += draw_points

sorted_league = sorted(league_table.items(), key=lambda x: x[1], reverse=True)

print("Final table: ")
for position, (team, points) in enumerate(sorted_league, start=1):
    print(f"{position}. {team} - {points} pts")
