from config import db, ma
from marshmallow_sqlalchemy import ModelSchema

class WinePairing(db.Model):
    __tablename__ = 'wine_pairing'
    id = db.Column(db.Integer, primary_key=True)
    wine = db.Column(db.String(32),)
    wine_description = db.Column(db.String(32))
    cheese = db.Column(db.String(32))
    cheese_description = db.Column(db.String(32))
    pairing_notes = db.Column(db.String(32))

class WinePairingSchema(ModelSchema):
    class Meta:
        model = WinePairing
        sqla_session = db.session
