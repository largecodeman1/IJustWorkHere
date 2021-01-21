#(Note: Need to update API Key every 24 hours)
import requests
import json

def JSON_PrettyPrint(json_object):
    return print(json.dumps(json_object, indent=2))

#AccountId = input("what is the Summoner name: ")

AccountId = 'psy6'

#APIQuery('psy6')

def APIQuery(AccountId):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + AccountId + "?api_key=RGAPI-YOUR-API-KEY"

    payload={}

    API_Key = "RGAPI-87bfb818-751e-4b7a-ab23-d4b9d12375c9"

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
    #JSON_PrettyPrint(json_object)


    #for match in json_object['matches']:
    gameId = json_object['matches'][0]['gameId']
    #JSON_PrettyPrint(match)
    #gameId = match['gameId']
    print("gameId: " + str(gameId))

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
            #goldEarned = participant['player']['goldEarned']
            break
        else:
            continue
    print("participantId:" + str(participantId))
    for participantId_data in json_object['participants']:
        #print("Match Id for participant: " + str(participantId_data))
        #JSON_PrettyPrint(participantId_data)
        if participantId == participantId_data['participantId']:
            print("Match Id for participant: " + str(participantId_data))
            #JSON_PrettyPrint(participantId_data)
            championId = int(participantId_data['championId'])
            goldEarned = int(participantId_data['stats']['goldEarned'])
            print("championId: " + str(championId))
            print("profileIcon: " +str(profileIcon))
            print("goldEarned: " +str(goldEarned))
            break
            #print("profileIcon: " + str(profileIcon))
            #print("Total Time cc: " + str(totalTimeCrowdControlDealt))
            #totalTimeCrowdControlDealt = int(participantId_data['totalTimeCrowdControlDealt'])
    result = {'gameId': gameId, 'participantId': participantId, 'championId': championId, 'profileIcon': profileIcon, 'goldEarned': goldEarned}
    #result = {'gameId': '3730386044', 'participantId': 6, 'championId': 200, 'goldEarned': 8970}
    return(result)
#APIQuery(AccountId)

def test_transfer_data1(test):
    test = {'gameId': '3730386044', 'participantId': 6, 'championId': 200, 'profileIcon': 10, 'goldEarned': 8970}
    return test

def clear_data():
    test = {'gameId': '','participantId': '', 'championId': '', 'profileIcon': '', 'goldEarned': ''}
    return test




if __name__ == "__main__":
    AccountId = 'psy6'
    APIQuery(AcountID)





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
