from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect
import pprint
import sys

app = Flask(__name__)

''' database setup  '''
dbURI = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

''' table definitions '''


class Players(db.Model):
    accountId = db.Column(db.String(255), primary_key=True, nullable=False)
    encryptedId = db.Column(db.String(255), nullable=False)
    matchListData = db.Column(db.Text, nullable=False)


class Matches(db.Model):
    matchId = db.Column(db.Integer, primary_key=True, nullable=False )
    matchData = db.Column(db.Text, nullable=False)

def addPlayer(AccountId, EncryptedId, gameId_list):
    player = Players.query.filter_by(accountId=AccountId).first()
    print(player)
    #return User.query.get(int(user_id))
    if player and player.accountId == AccountId:
        #print("Updating data for User " + player.accountId + " with data " + gameId_list)
        player.matchListData = gameId_list
        db.session.commit()

    else:
        new_player = Players(accountId=AccountId, encryptedId=EncryptedId, matchListData=gameId_list)
        #print("Adding New User: " + new_player.accountId + " with data:" + gameId_list)
        db.session.add(new_player)
        db.session.commit()

def addMatch(MatchId, MatchData):
    match = Matches.query.filter_by(matchId=MatchId).first()

    # Error Checking
    if match and match.matchId == MatchId:
        try:
            if match.matchData.find('gameId'):
                return True
            else:
                # corrupted Key in DB
                match.matchData=str(MatchData)
                db.session.commit()
                return False
        except:
            e = sys.exc_info()[0]
            print("Error in JSON format: {0}".format(e))
            print("isRiotMatchDataInDB Something wrong with API Call!"+str(match.matchId))
            pprint.pprint(match.matchData)
    else:
        if MatchData.find('gameId'):
            # Probably good data
            new_match = Matches(matchId=MatchId, matchData=str(MatchData))
            db.session.add(new_match)
            db.session.commit()
            return True

    return False



def isEncryptedIdInDB(AccountId):
    player = Players.query.filter_by(accountId=AccountId).first()
    #return User.query.get(int(user_id))
    if player and player.accountId == AccountId:
        return True
    else:
        return False

def getEncryptedIdInDB(AccountId):
    player = Players.query.filter_by(accountId=AccountId).first()
    #return User.query.get(int(user_id))
    if player and player.accountId == AccountId:
        return player.encryptedId

    return False

def isRiotMatchDataInDB(MatchId):
    match = Matches.query.filter_by(matchId=MatchId).first()
    if match and match.matchId == MatchId:
        # Check if valid data or throw it out
        try:
            if match.matchData.find('gameId'):
                #print("Should be good")
                return True
            else:
                return False
        except:
            e = sys.exc_info()[0]
            print("Error in JSON format: {0}".format(e))
            print("isRiotMatchDataInDB Something bad with API Call!"+str(match.matchId))
            pprint.pprint(match.matchData)

    return False

def getRiotMatchDataInDB(MatchId):
    match = Matches.query.filter_by(matchId=MatchId).first()
    if match and match.matchId == MatchId:
        return match.matchData
    return False

''' table creation '''
db.create_all()

''' inspect table '''
engine = create_engine(dbURI)
insp = inspect(engine)
for name in insp.get_table_names():
    print("Table " + str(name))
