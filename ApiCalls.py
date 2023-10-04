import requests
import json

team_dictionary = {
    "ATL": "1",
    "BUF": "2",
    "CHI": "3",
    "CIN": "4",
    "CLE": "5",
    "DAL": "6",
    "DEN": "7",
    "DET": "8",
    "GB": "9",
    "TEN": "10",
    "IND": "11",
    "KC": "12",
    "LV": "13",
    "LAR": "14",
    "MIA": "15",
    "MIN": "16",
    "NE": "17",
    "NO": "18",
    "NYG": "19",
    "NYJ": "20",
    "PHI": "21",
    "ARI": "22",
    "PIT": "23",
    "LAC": "24",
    "SF": "25",
    "SEA": "26",
    "TB": "27",
    "WSH": "28",
    "CAR": "29",
    "JAX": "30",
}

def get_week(arg):
    week_response = requests.get("https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/weeks/"+str(arg)+"/events")
    week_json_data = json.loads(week_response.text)

    game_week = []

    for weekgames in week_json_data["items"]:
        str_games = str(weekgames)
        str_games = str_games[10:-2]
        game_response = requests.get(str_games)
        game_json_data = json.loads(game_response.text)
        game = game_json_data["shortName"] + " - " + game_json_data["date"]
        game_week.append(game)
        nfl_games = "\n".join([str(elem) for elem in game_week])
    return(nfl_games)

def get_week_team(x, y):
    week = int(x) - 1
    week = str(week)
    teamId = team_dictionary.get(y)
    response = requests.get("http://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/"+ teamId + "/schedule?season=2023")
    team_games_json = json.loads(response.text)
    team_week = team_games_json["events"][int(week)]
    game = team_week["shortName"] + " - " + team_week["date"]
    return(game)



