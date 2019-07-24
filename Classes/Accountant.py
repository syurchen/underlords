class Accountant:

    _levelExp = {
        1:  1,
        2:  1,
        3:  1,
        4:  1,
        5:  4,
        6:  8,
        7:  16,
        8:  24,
        9:  32,
        10: 40
    }
    _levelChances = {
        1: (1,  0,  0,  0,  0),
        2: (.70,.30, 0,  0,  0),
        3: (.6, .35, .5, 0,  0),
        4: (.5, .35,.15, 0,  0),
        5: (.4, .35,.23,.02, 0),
        6: (.33,.3 ,.3 ,.07, 0),
        7: (.30,.30,.30,.10, 0),
        8: (.24,.30,.30,.15, .01),
        9: (.22,.25,.30,.20, .03),
        10:(.19,.25,.25,.25, .06),
        11:(.13,.20,.25,.30, .12)
    }
    _poolSize = {
        1: 45,
        2: 30,
        3: 25,
        4: 15,
        5: 10
    }


    _playerLevel = 1
    _playerGold = 0
    #Exp towards next level
    _playerExp = 0


    def __init__(self, oHeroFactory, playerLevel, playerS, opponentS):
        self._playerS = playerS
        self._opponentS = opponentS
        self._playerLevel = playerLevel

        self._sharedPool = HeroStorage()
        oHeroFactory.doWithEveryHero(populateSharedPool)
       
    #This method will only be used in constructor
    def populateSharedPool(hero):
        heroName = hero.getName()
        self._sharedPool[heroName] -= playerS.getHeroCount(heroName)
        self._sharedPool[heroName] -= opponentS.getHeroCount(heroName)

    def getLevelUpCost(self):
        return getLevelUpCost(self._playerLevel + 1, self._playerExp)

    def getLevelUpCost(levelTG, playerExp = 0):
        expDelta = Accountant._levelExp[levelTG] - playerExp
        return round(expDelta / 4) * 5
        

    def getUpgradeChance(self, hero):
        return

