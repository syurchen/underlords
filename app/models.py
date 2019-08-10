from app import db
from sqlalchemy.types import PickleType

class scoreboard(db.Model):
    __tablename__ = 'scoreboards'
    id = db.Column(db.Integer, primary_key=True)
    old_file = db.Column(db.String(128))
    new_file = db.Column(db.String(128))
    parsed_result = db.Column(PickleType)


