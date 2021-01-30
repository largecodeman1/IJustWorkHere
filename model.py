class Users(db.Model):
    accountId = db.Column(db.text, nullable=False)
    encryptedId = db.Column(db.text, nullable=False)
    matchId = db.Column(db.text, nullable=False)


class Matches(db.Model):
    matchId = db.Column(db.text, nullable=False)
    matchdata = db.Column(db.Text, nullable=False)

