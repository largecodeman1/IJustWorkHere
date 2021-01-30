from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect

app = Flask(__name__)

''' database setup  '''
dbURI = 'sqlite:///riot.db'
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

    #return User.query.get(int(user_id))
    if match and match.matchId == MatchId:
        print("Already in the Database")
        # print('MatchId argument is: ' + str(MatchId))
        # print('MatchId from query is: ' + str(match.matchId))
    else:
        new_match = Matches(matchId=MatchId, matchData=str(MatchData))
        # print("Adding New Match: " + str(new_match.matchId))
        db.session.add(new_match)
        db.session.commit()



''' table creation '''
db.create_all()

''' inspect table '''
engine = create_engine(dbURI)
insp = inspect(engine)
for name in insp.get_table_names():
    print("Table " + str(name))
