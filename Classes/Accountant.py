from Classes.HeroPack import HeroStorage
import scipy.special

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
        self._playerLevel = int(playerLevel)
        self._heroFactory = oHeroFactory

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
        #now we should extract blacklist (heroes that are shown to you right now)
        return odds

    def getPoolCountByCost(self, heroCost):
        #TODO remove 3 stars that player has
        poolCount = 0
        heroList = self._heroFactory.getHeroListByCost(heroCost)
        for heroName in heroList:
            poolCount += self._sharedPool.getHeroCount(heroName)

        return poolCount

    # returns Dict with upgrade chances per roll number (default 5, 10, 15)
    def getUpgradeChanceFixedRolls(self, heroName):
        hero = self._heroFactory.getHeroByName(heroName)

        heroCost = hero.getCost()
        playerCount = self._playerS.getHeroCount(heroName)
        poolCount = self.getPoolCountByCost(heroCost) 
        costOdds = Accountant.getOdds(self._playerLevel)[heroCost - 1]
        if playerCount < 3:
            upgradeCount = 3 - playerCount
        else:
            upgradeCount = 9 - playerCount
        
        chances = {5: 0, 10: 0, 15: 0}
        print(upgradeCount, poolCount)

        for i in chances.keys():
            rollCount = i * 5 #because we are displayer 5 heroes per roll
            chance = 10000 * costOdds * scipy.special.binom(poolCount - upgradeCount, rollCount - upgradeCount) / scipy.special.binom(poolCount, rollCount)
            chances[i] = chance
        return chances
