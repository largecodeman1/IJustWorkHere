import requests
import json

def JSON_PrettyPrint(json_object):
    return print(json.dumps(json_object, indent=2))

#AccountId = input("what is the Summoner name: ")

# Default Setting
AccountId = 'psy6'

#
# NOTE: NEED TO UPDATE THIS EVERY 7 HOURS - Call Zach or create your own account on developer.riotgames.com
#
API_Key = "RGAPI-87bfb818-751e-4b7a-ab23-d4b9d12375c9"

# Get Riot test data for mid-term and after put into database
def APIQuery(AccountId):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + AccountId + "?api_key=RGAPI-YOUR-API-KEY"

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

    url = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + summoner_accountId

    payload={}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except:
        print("Error with API")
        return clear_data()

    json_data = response.text

    json_object = json.loads(json_data)

    #JSON_PrettyPrint(json_object)

    # NOTE for demo just use the first match we find and get the data for the mid-term

    #for match in json_object['matches']:
    gameId = json_object['matches'][0]['gameId']
    #JSON_PrettyPrint(match)
    #gameId = match['gameId']
    print("gameId: " + str(gameId))

    base_url = "https://na1.api.riotgames.com/lol/match/v4/matches/"

    game_url = base_url + str(gameId)
    payload={}

    # TODO add error checking when making generic riot_api request function call

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
    # TDOD Debug code to delete later
    #result = {'gameId': '3730386044', 'participantId': 6, 'championId': 200, 'goldEarned': 8970}
    return(result)

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
    APIQuery(AcountID)


