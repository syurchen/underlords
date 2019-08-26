#!/usr/bin/env python3
from app import db
from app.models import Scoreboard
from Classes.Methods import storeParsedData, detect

if __name__ == "__main__":
    s = Scoreboard.query.filter(Scoreboard.parsed_player_level == None).first()
    if s != None:
        #should store as array. not as class
        playerLevel, playerS, opponentS = detect(s.old_file, s.new_file)
        if playerLevel > 0:
            playerS = playerS.toArray()
            opponentS = opponentS.toArray()
        storeParsedData(s.old_file, s.new_file, playerLevel, playerS,
                        opponentS)
