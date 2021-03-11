#Sudo code
# 1. find encrypted summoner Id
# 2. find match Id list
# 3. record AccountId, Match Id, and Encrypted summoner Id
# 4. Use Match Id to query json
# 5. record json in data base
from create_riot_db import app, db, Players, Matches, addPlayer, addMatch, isEncryptedIdInDB, getEncryptedIdInDB, isRiotMatchDataInDB, getRiotMatchDataInDB
import requests
import json
import pprint
import sys


def JSON_PrettyPrint(json_object):
    return print(json.dumps(json_object, indent=2))

#AccountId = input("what is the Summoner name: ")

# Default Setting
AccountId = 'psy6'

#
# NOTE: NEED TO UPDATE THIS EVERY 24 HOURS - Call Zach or create your own account on developer.riotgames.com
#
API_Key = "RGAPI-a083ab17-7c97-4adc-8b6a-84483539bffc"

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
    This was painful ... this s the API Key error:

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
        return False

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
        return "",clear_data()

    json_data = response.text

    json_object = json.loads(json_data)

    # NOTE for demo just use the first match we find and get the data for the mid-term
    count = -1
    gameId_list = []
    match_list_data = {}
    try:
        if json_object['matches']:
            print("Found it!")
    except KeyError as e:
        print("ERROR WITH API: Missing field: {0}".format(e))
        # Use was is in the DB

        return "",clear_data()

    match_list_data = {}
    for match_data_single_player in json_object['matches']:
        count+=1
        # stop after 10
        if count > 10:
            break


        gameId = match_data_single_player['gameId']
        gameId_list.append(gameId)
        timestamp = match_data_single_player['timestamp']
        lane = match_data_single_player['lane']


       # match_list_data[gameId, 'timestamp'] = timestamp
       # match_list_data[gameId, 'lane'] = lane
       # match_list_data[gameId, 'match_data'] = match_data_single_player
        new_data = { 'gameId' : { 'timestamp' : timestamp, 'lane' : lane, 'match_data' : match_data_single_player } }
        match_list_data.update(new_data)
        #print('count: ' + str(count))
#       pprint.pprint(match_list_data)

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
    #pprint.pprint(json_data)

    return json_data # Match data raw


def Riot_Match_data_parse(summoner_accountId, gameId, match_json_data):

    match_data = {}
    if match_json_data:
        try:
            json_object = json.loads(match_json_data)
        except:
            e = sys.exc_info()[0]
            print("Error in JSON format: {0}".format(e))
            return clear_data()
        try:
            if json_object and json_object['participantIdentities']:
                print()
            else:
                return clear_data()
        except KeyError as e:
            print("SKIPPING: Missing field: {0}".format(e))
            return clear_data()
    else:
        return clear_data()
    for participant in json_object['participantIdentities']:
        if summoner_accountId == participant['player']['accountId']:
            participantId = participant['participantId']
            profileIcon = participant['player']['profileIcon']
            break
        else:
            continue

    for participantId_data in json_object['participants']:
        if participantId == participantId_data['participantId']:

            championId = int(participantId_data['championId'])
            goldEarned = int(participantId_data['stats']['goldEarned'])
            visionScore = float(participantId_data['stats']['visionScore'])
            deaths = int(participantId_data['stats']['deaths'])
            kills = int(participantId_data['stats']['kills'])
            damageDealtToTurrets = float(participantId_data['stats']['damageDealtToTurrets'])
            totalMinionsKilled = int(participantId_data['stats']['totalMinionsKilled'])
            break
    match_data[gameId] = {'gameId': gameId, 'participantId': participantId, 'championId': championId, 'profileIcon': profileIcon, 'goldEarned': goldEarned, 'visionScore': visionScore, 'deaths': deaths, 'kills': kills, 'damageDealtToTurrets': damageDealtToTurrets, 'totalMinionsKilled': totalMinionsKilled, }

    return(match_data)

# Test function for web development
def test_transfer_data1(test):
    test = {'gameId': '3730386044', 'participantId': 6, 'championId': 200, 'profileIcon': 10, 'goldEarned': 8970}
    return test

# function for riot_api_test page
def clear_data():
    test = {'gameId': '','participantId': '', 'championId': '', 'profileIcon': '', 'goldEarned': ''}
    return test

def Riot_API_Data(AccountId):
    # Find Account Id in Database if not get it from the cloud
    if isEncryptedIdInDB(AccountId):
        EncryptedId = getEncryptedIdInDB(AccountId)
    else:
        EncryptedId = Riot_Encrypted_Id(AccountId)

    if (EncryptedId):
        # Get latest Riot Data and update DB
        # TODO: IF API QUERY FAILS JUST USE DB DATA
        gameId_list, match_list_data = Riot_Matchlist(EncryptedId)
        test = json.dumps(match_list_data)
        addPlayer(AccountId, EncryptedId, test)

        return_match_data = {}
        for gameId in gameId_list:
            if isRiotMatchDataInDB(gameId):
                # Found in db
                match_data = getRiotMatchDataInDB(gameId)
            else:
                # get from cloud and store in DB
                match_data = Riot_Match_data(EncryptedId,gameId)
                addMatch(gameId, str(match_data))
            parsed_data = Riot_Match_data_parse(EncryptedId,gameId,match_data)
            return_match_data.update(parsed_data)

        return return_match_data

    return_match_data = clear_data()

    return_match_data['gameId'] = f"ERROR: I think you may have fat fingered the username: \"{AccountId}\" ...  TRY AGAIN!"

    return return_match_data

def Riot_API_Data_By_Match(AccountId,MatchId):
    # Find Account Id in Database if not get it from the cloud
    if isEncryptedIdInDB(AccountId):
        EncryptedId = getEncryptedIdInDB(AccountId)
    else:
        EncryptedId = Riot_Encrypted_Id(AccountId)

    if (EncryptedId):
        # Get latest Riot Data and update DB
        # TODO: IF API QUERY FAILS JUST USE DB DATA
        gameId_list, match_list_data = Riot_Matchlist(EncryptedId)
        test = json.dumps(match_list_data)
        addPlayer(AccountId, EncryptedId, test)

        return_match_data = {}

        if isRiotMatchDataInDB(MatchId):
            # Found in db
            match_data = getRiotMatchDataInDB(MatchId)
        else:
            # get from cloud and store in DB
            match_data = Riot_Match_data(EncryptedId,MatchId)
            addMatch(MatchId, str(match_data))
        return_match_data = Riot_Match_data_parse(EncryptedId,MatchId,match_data)


        return return_match_data

    return clear_data()

    return return_data

def Riot_API_Data_Get_From_DB(AccountId):
    EncryptedId = Riot_Encrypted_Id(AccountId)
    gameId_list, match_list_data = Riot_Matchlist(EncryptedId)
    gameId_list_str = ','.join(gameId_list)
    addPlayer(AccountId, EncryptedId, gameId_list_str)

    return_data
    for gameId in gameId_list:
        match_data = Riot_Match_data(EncryptedId,gameId)
        addMatch(gameId, str(match_data))
        parsed_data = Riot_Match_data_parse(EncryptedId,gameId,match_data)
        return_data.update(parsed_data)

    return return_data




    # Default account code
if __name__ == "__main__":

    AccountId = 'psy6'
    #AccountId = 'dracus1234567'
    # EncryptedId = Riot_Encrypted_Id(AccountId)
    # print(EncryptedId)
    # pprint.pprint('EncryptedId:' + EncryptedId)
    # gameId_list, match_list_data = Riot_Matchlist(EncryptedId)
    # test = json.dumps(match_list_data)
    # addPlayer(AccountId, EncryptedId, test)
    #
    # for gameId in gameId_list:
    #     match_data = Riot_Match_data(EncryptedId,gameId)
    #     addMatch(gameId, str(match_data))
    #     parsed_data = Riot_Match_data_parse(EncryptedId,gameId,match_data)

    riot_data = Riot_API_Data(AccountId)

    pprint.pprint(riot_data)

    Summoner_Id_data = clear_data()
    # POST redirection to content page
    name = AccountId
    match = 3818324657
    if name != "":
        Summoner_Id_data = Riot_API_Data_By_Match(name,match)
    r = json.dumps(Summoner_Id_data)
    loaded_r = json.loads(r)
    pprint.pprint(loaded_r)
