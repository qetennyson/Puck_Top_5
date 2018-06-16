import requests
import json

from collections import namedtuple, defaultdict

# Pulls in all Puck players
puck_players = requests.get('https://api.opendota.com/api/heroes/13/players')

# Decodes JSON for use in Python
players_parsed = json.loads(puck_players.text)

PlayerData = namedtuple('Player', 'WinRatio')

top_players = []

for player in players_parsed:
    games = player["games_played"]
    id = player["account_id"]
    wins = player["wins"]

    if games > 80:
        account_names = requests.get('https://api.opendota.com/api/players/{}'.format(id))
        accounts_parsed = json.loads(account_names.text)
        player_name = accounts_parsed["profile"]["name"]

        win_ratio = "{0:.2%}".format(wins / games)
        PlayerData = (player_name, win_ratio)
        top_players.append(PlayerData)




