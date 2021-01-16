#(Note: Need to update API Key every 24 hours)
import requests
import json

def JSON_PrettyPrint(json_object):
    return print(json.dumps(json_object, indent=2))

#AccountId = input("what is the Summoner name: ")
AccountId = 'psy6'

url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + AccountId + "?api_key=RGAPI-YOUR-API-KEY"

payload={}

API_Key = "RGAPI-e4e3243b-8da3-455c-b376-30fa025293ec"

headers = {
    'X-Riot-Token': API_Key
}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = response.text

json_object = json.loads(json_data)

summoner_accountId = json_object['accountId']

url = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + summoner_accountId

payload={}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = response.text

json_object = json.loads(json_data)

base_url = "https://na1.api.riotgames.com/lol/match/v4/matches/"

for match in json_object['matches']:



    #JSON_PrettyPrint(match)
    gameId = match['gameId']
    #print(gameId)

    game_url = base_url + str(gameId)
    payload={}

    response = requests.request("GET", game_url, headers=headers, data=payload)

    json_data = response.text

    json_object = json.loads(json_data)

    #JSON_PrettyPrint(json_object)

    for participant in json_object['participantIdentities']:
        print("participantIdentities:" + str(participant))
        #print(participant['player']['accountId'])
        if summoner_accountId == participant['player']['accountId']:
            participantId = participant['participantId']
            profileIcon = participant['player']['profileIcon']
            break
        else:
            continue
    print("participantId:" + str(participantId))
    for participantId_data in json_object['participants']:
        #print("Match Id for participant: " + str(participantId_data))
        #JSON_PrettyPrint(participantId_data)
        if participantId == participantId_data['participantId']:
            print("Match Id for participant: " + str(participantId_data))
            JSON_PrettyPrint(participantId_data)
            championId = int(participantId_data['championId'])
            #profileIcon = int(participantId_data['profileIcon'])
            print("championId: " + str(championId))
            print("profileIcon: " +str(profileIcon))
            #print("profileIcon: " + str(profileIcon))
            #print("Total Time cc: " + str(totalTimeCrowdControlDealt))
            #totalTimeCrowdControlDealt = int(participantId_data['totalTimeCrowdControlDealt'])
    exit(1)


















# matchId = input("what is the match id: ")
# AccountName = input("what is the Summoner name: ")
# #url = "https://na1.api.riotgames.com/lol/match/v4/matches/" + matchId
# #url = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/6Yh6lfoea3Ceg4xAHxTyI0I7NHLdWq3v_JcV-ZaWM78Dzr4Gl3Lxvwws"
# url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + AccountName + "?api_key=RGAPI-YOUR-API-KEY"
# payload={}
#
# # test match id 3685845648
#
# #Need to update every time I run this
# API_Key = "RGAPI-11f2ef26-b328-41f3-ae27-7b0303728c3b"
#
# headers = {
#     'X-Riot-Token': API_Key
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# json_data = response.text
#
# json_object = json.loads(json_data)
#
# json_formatted_str = json.dumps(json_object, indent=2)
#
# print(json_formatted_str)
#
# #print(response.text)
