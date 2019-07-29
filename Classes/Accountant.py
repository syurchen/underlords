from Classes.HeroPack import HeroStorage
from functools import partial

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
    _opponents = {}


    def __init__(self, oHeroFactory, playerLevel, playerS, opponentS, opponents = {}):
        self._playerS = playerS
        self._opponentS = opponentS
        self._playerLevel = int(playerLevel)
        self._heroFactory = oHeroFactory
        self._opponents = opponents

        self._sharedPool = HeroStorage()
        oHeroFactory.doWithEveryHero(self.populateSharedPool)
       
    #This method will only be used in constructor
    def populateSharedPool(self, hero):
        heroName = hero.getName()
        count = self._poolSize[hero.getCost()]

        count -= self._playerS.getHeroCount(heroName)
        count -= self._opponentS.getHeroCount(heroName)

        self._sharedPool.store(hero, count)

    def getLevelUpCost(self):
        return getLevelUpCost(self._playerLevel + 1, self._playerExp)

    def getLevelUpCost(levelTG, playerExp = 0):
        expDelta = Accountant._levelExp[levelTG] - playerExp
        return round(expDelta / 4) * 5
        

    def getOdds(playerLevel):
        odds = Accountant._levelChances[playerLevel]
        return odds

    def getPoolCountByCost(self, heroCost):
        poolCount = 0
        heroList = self._heroFactory.getHeroListByCost(heroCost)
        #removing 3 stars that player has, because this unit wont be shown
        completedList = []
        self._playerS.doWithEveryStoredHero(partial(Accountant.getCompleted, completedList))
        #TODO we should extract blacklist (heroes that are shown to you right now) need opponent count and levels for this

        for heroName in heroList:
            if heroName not in completedList:
                poolCount += self._sharedPool.getHeroCount(heroName)

        return poolCount

    def getCompleted(completedList, heroDict):
        if heroDict['count'] == 9:
            completedList.append(heroDict['name'])

    # returns Dict with upgrade chances per roll number (default 5, 10, 15)
    def getUpgradeChanceFixedRolls(self, heroName):
        hero = self._heroFactory.getHeroByName(heroName)

        heroCost = hero.getCost()
        playerCount = self._playerS.getHeroCount(heroName)
        poolCount = self.getPoolCountByCost(heroCost) #Number of heroes on same cost in pool
        heroPoolCount = self._sharedPool.getHeroCount(heroName) #Number of desired heroes in pool
        costOdds = Accountant.getOdds(self._playerLevel)[heroCost - 1]
        if playerCount < 3:
            upgradeCount = 3 - playerCount
        else:
            upgradeCount = 9 - playerCount
        
        chances = {5: 0, 10: 0, 15: 0}

        mainChance = 1
        for i in range (0, upgradeCount - 1):
            mainChance = mainChance * (heroPoolCount - i) / (poolCount - i) 
        mainChance = mainChance * costOdds

        for i in chances.keys():
            rollCount = i * 5 #because we are displayer 5 heroes per roll
            chance = round(mainChance * (rollCount - upgradeCount) * 10**6, 3)
            if chance > 100:
                chances[i] = 99.999
            else:
                chances[i] = chance
        return chances
