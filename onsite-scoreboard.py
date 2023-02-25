import requests

online_teams = requests.get('http://51.75.140.42/api/v1/scoreboard').json()["data"]
with open("onsite.csv", "r") as file:
    lines = [line.split(",") for line in file.readlines()[1:]]
    onsite_teams = {x[0]:int(x[1]) for x in lines}

final_scoreboard = {}

for team in online_teams:
    if team["name"] in onsite_teams:
        final_scoreboard[team["name"]] = onsite_teams[team["name"]] + team["score"]

final_scoreboard = {k: v for k, v in sorted(final_scoreboard.items(), key=lambda item: item[1])}
for k,v in final_scoreboard.items():
    print(f"{k}: {v}")