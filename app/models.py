from app import db
from sqlalchemy.types import PickleType

class Scoreboard(db.Model):
    __tablename__ = 'scoreboards'
    id = db.Column(db.Integer, primary_key=True)
    old_file = db.Column(db.String(128))
    new_file = db.Column(db.String(128))
    parsed_result = db.Column(PickleType) #Calculated result for 5, 10 and 15 rolls
#Heroes' storages detected on image
    parsed_player_level = db.Column(db.Integer)
    parsed_player_storage = db.Column(PickleType) 
    parsed_opponent_storage = db.Column(PickleType) 


