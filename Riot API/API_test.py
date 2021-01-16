import requests
import json
matchId = input("what is the match id: ")
AccountName = input("what is the Summoner name: ")
url = "https://na1.api.riotgames.com/lol/match/v4/matches/" + matchId
#url = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/6Yh6lfoea3Ceg4xAHxTyI0I7NHLdWq3v_JcV-ZaWM78Dzr4Gl3Lxvwws"
#url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + AccountName + "?api_key=RGAPI-YOUR-API-KEY"
payload={}

# test match id 3685845648

#Need to update every time I run this
API_Key = "RGAPI-11f2ef26-b328-41f3-ae27-7b0303728c3b"

headers = {
    'X-Riot-Token': API_Key
}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = response.text

json_object = json.loads(json_data)

json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)

#print(response.text)
