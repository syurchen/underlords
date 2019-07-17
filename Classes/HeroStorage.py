from Classes import Utils, Hero 

class HeroStorage:
    
    _storage = {}
   
    # All heroes are stored in tokens (1*)
    def store(hero):
        heroName = hero.getName()
        heroDict = {}
        heroDict.hero, heroDict.count = hero.tokenize()
        if heroName in _storage:
            _storage[heroName].count += heroDict.count
        else:
            _storage[heroName] = heroDict

    def getHeroCount(self, heroName):
        try:
            return _storage[heroName].count
        except:
            return 0

