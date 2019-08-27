from Classes.Utils import Utils
import json

class Hero:
    _name = ''
    _cost = 1
    _star = 1

    _iconPath = ''
    _iconFolder = ''

    def __init__(self, name, cost, iconFolder, star = 1, hard = False):
        self._name = name
        self._cost = cost
        self._star = star
        self._iconFolder = iconFolder
        self.hard = hard

    def getIcon(self):
        if self._iconPath != '':
            return self._iconPath
        else:
            self._iconPath = Utils.OsFind(self._name.replace(' ', '_') + '*', self._iconFolder) 
            return self._iconPath

    def getName(self):
        return self._name

    def getCost(self):
        return self._cost

    def getStar(self):
        return self._star

    def tokenize(self):
        count = 3 ** (self._star - 1)
        self._star = 1
        return self, count

class HeroFactory:
    #Should probably be in config

    _heroIconFolder = ''
    _heroList = []
    # These units will be detected with special rules
    _hardDetection = [
        'Timbersaw',
        'Necrophos',
        'Viper',
        'Terrorblade',
        'Troll Warlord'
    ]

    def __init__(self, heroIconFolder, jsonFile):
        self._heroIconFolder = heroIconFolder
        self.count = 0
        with open(jsonFile, 'r') as f:
            heroesFull = json.load(f)
            f.close()
        for name, hero in heroesFull.items():
            if hero['draftTier'] == 0: #it's a summon
                continue
            name = Utils.prepareHeroName(name)
            if name in self._hardDetection:
                hard = True
            else:
                hard = False

            self._heroList.append({
                'name': name,
                'cost': hero['goldCost'],
                'alliances': hero['keywords'].split(),
                'hard': hard
            })

    def getHeroListByCost(self, cost):
        heroList = []
        for hero in self._heroList:
            if hero['cost'] == cost:
                heroList.append(hero['name'])
        return heroList

    def getHeroByName(self, name, star = 1):
        heroDict = next((x for x in self._heroList if x['name'] == name), None)
        return Hero(heroDict['name'], heroDict['cost'], self._heroIconFolder, star, heroDict['hard'])

    def doWithEveryHero(self, func):
        for heroDict in self._heroList:
            func(Hero(heroDict['name'], heroDict['cost'], self._heroIconFolder, 1, heroDict['hard']))
                #self.count += 1

class HeroStorage:
    
    def __init__(self, storage = None):
        if storage is None:
            self._storage = {}
        else:
            self._storage = storage

    # All heroes are stored in tokens (1*)
    def store(self, hero, count = 0):
        heroName = hero.getName()
        if count == 0:
            hero, count = hero.tokenize()
        if heroName in self._storage:
            self._storage[heroName]['count'] += count
        else:
            self._storage[heroName] = {'name': heroName, 'count': count}

    def getHeroCount(self, heroName):
        try:
            return self._storage[heroName]['count']
        except:
            return 0

    def doWithEveryStoredHero(self, func):
        for hero in self._storage.values():
            func(hero)

    def toArray(self):
        return self._storage

