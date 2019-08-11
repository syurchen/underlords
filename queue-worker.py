#!/usr/bin/env python3
from app import db
from app.models import Scoreboard
from Classes.Methods import storeResults, getResultsByNewImg, detectAndCalculate

if __name__ == "__main__":
    s = Scoreboard.query.filter(Scoreboard.parsed_result == None).first()
    if s != None:
        chancesList = detectAndCalculate(s.old_file, s.new_file)
        s.parsed_result = chancesList
        db.session.commit()
