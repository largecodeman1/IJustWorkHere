#Sudo code
# 1. find encrypted summoner Id
# 2. find match Id list
# 3. record AccountId, Match Id, and Encrypted summoner Id
# 4. Use Match Id to query json
# 5. record json in data base
from create_riot_db import app, db, Players, Matches, addPlayer, addMatch
import requests
import json
import pprint

def JSON_PrettyPrint(json_object):
    return print(json.dumps(json_object, indent=2))

#AccountId = input("what is the Summoner name: ")

# Default Setting
AccountId = 'psy6'

#
# NOTE: NEED TO UPDATE THIS EVERY 24 HOURS - Call Zach or create your own account on developer.riotgames.com
#
API_Key = "RGAPI-ca24cc7a-9a18-4526-bf45-61e2301852c8"

# Get Riot test data for mid-term and after put into database
def Riot_Encrypted_Id(AccountId):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + AccountId #+ "?api_key=RGAPI-YOUR-API-KEY"
    result = {}
    payload={}

    # API V4 required API_Key to be in the header.  This sucked to figure out!
    headers = {
        'X-Riot-Token': API_Key
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except:
        print("Error with API")
        return clear_data()

    json_data = response.text

    json_object = json.loads(json_data)

    """
    This was painful ... this was the API Key error:

    {
      "status": {
        "message": "Forbidden",
        "status_code": 403
      }
    }

    TODO Since there is going be 1000s API calla need make a function with error checking.

    """

    # Check to see if forbidden response from server
    if 'status' in json_object and json_object['status']['status_code'] == 403:
        print("Error with API ... Probably API Key needs updating")
        data = clear_data()
        data['gameId'] = 'D\'OH! ERROR: Call Zach to update the API KEY AGAIN!'
        return data

    # Check to see if valid response from server with the AccountId needed
    if 'accountId' not in json_object:
        print("Error with API ... Probably BAD AccountId")
        data = clear_data()
        data['gameId'] = f"ERROR: I think you may have fat fingered the username: \"{AccountId}\" ...  TRY AGAIN!"
        return data

    # Use account number to get all the matches player was ever in, could be ton
    summoner_accountId = json_object['accountId']
    return summoner_accountId

def Riot_Matchlist(summoner_accountId):

    url = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + summoner_accountId

    payload={}

    headers = {
        'X-Riot-Token': API_Key
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except:
        print("Riot_Matchlist: Error with API")
        return clear_data()

    json_data = response.text

    json_object = json.loads(json_data)

    #JSON_PrettyPrint(json_object)

    # NOTE for demo just use the first match we find and get the data for the mid-term
    count = -1
    gameId_list = []
    match_list_data = {}
    for match in json_object['matches']:
        count+=1
        # stop after 10
        if count > 100:
            break


        gameId = match['gameId']
        gameId_list.append(gameId)
        timestamp = match['timestamp']
        lane = match['lane']


        match_list_data[gameId, 'timestamp'] = timestamp
        match_list_data[gameId, 'lane'] = lane
        match_list_data[gameId, 'match_data'] = match
        #print('count: ' + str(count))
        #pprint.pprint(match_list)

    return gameId_list, match_list_data



def Riot_Match_data(summoner_accountId, gameId):
    base_url = "https://na1.api.riotgames.com/lol/match/v4/matches/"

    game_url = base_url + str(gameId)
    payload={}

    # TODO add error checking when making generic riot_api request function call

    headers = {
        'X-Riot-Token': API_Key
    }

    try:
        response = requests.request("GET", game_url, headers=headers, data=payload)
    except:
        print("Riot_Match_data: Error with API")
        return clear_data()

    json_data = response.text
    json_object = json.loads(json_data)
    #JSON_PrettyPrint(json_object)
    match_data = {}
    if json_data:
        json_object = json.loads(json_data)
        if json_object and json_object['participantIdentities']:
            print()
        else:
            return clear_data()
    else:
        return clear_data()
    for participant in json_object['participantIdentities']:
        #print("participantIdentities:" + str(participant))
        #print(participant['player']['accountId'])
        if summoner_accountId == participant['player']['accountId']:
            participantId = participant['participantId']
            profileIcon = participant['player']['profileIcon']
            #goldEarned = participant['player']['goldEarned']
            break
        else:
            continue
    #print("participantId:" + str(participantId))
    for participantId_data in json_object['participants']:
        #print("Match Id for participant: " + str(participantId_data))
        #JSON_PrettyPrint(participantId_data)
        if participantId == participantId_data['participantId']:
            #print("Match Id for participant: " + str(participantId_data))
            #JSON_PrettyPrint(participantId_data)
            championId = int(participantId_data['championId'])
            goldEarned = int(participantId_data['stats']['goldEarned'])
            #print("championId: " + str(championId))
            #print("profileIcon: " +str(profileIcon))
            #print("goldEarned: " +str(goldEarned))
            break
            #print("profileIcon: " + str(profileIcon))
            #print("Total Time cc: " + str(totalTimeCrowdControlDealt))
            #totalTimeCrowdControlDealt = int(participantId_data['totalTimeCrowdControlDealt'])
    match_data[gameId] = {'gameId': gameId, 'participantId': participantId, 'championId': championId, 'profileIcon': profileIcon, 'goldEarned': goldEarned}
    # TDOD Debug code to delete later
    #result = {'gameId': '3730386044', 'participantId': 6, 'championId': 200, 'goldEarned': 8970}
    return(match_data)

# Test function for web development
def test_transfer_data1(test):
    test = {'gameId': '3730386044', 'participantId': 6, 'championId': 200, 'profileIcon': 10, 'goldEarned': 8970}
    return test

# function for riot_api_test page
def clear_data():
    test = {'gameId': '','participantId': '', 'championId': '', 'profileIcon': '', 'goldEarned': ''}
    return test

if __name__ == "__main__":
    # Test code
    #AccountId = input("what is the Summoner name: ")
    AccountId = 'psy6'
    EncryptedId = Riot_Encrypted_Id(AccountId)
    print(EncryptedId)
    pprint.pprint('EncryptedId:' + EncryptedId)
    gameId_list, match_list_data = Riot_Matchlist(EncryptedId)
    # pprint.pprint("gameId_list:")
    # pprint.pprint(gameId_list)
    # pprint.pprint("match_list_data:")
    addPlayer(AccountId, EncryptedId, 'gameId_list')

    # pprint.pprint(match_list_data)
    for gameId in gameId_list:
        #print("gameId:" + str(gameId))
        match_data = Riot_Match_data(EncryptedId, gameId)
        #print('match data:' + str(match_data))
        addMatch(gameId, str(match_data))




    # Riot_Match_data(match)
    # APIQuery(AcountID)
