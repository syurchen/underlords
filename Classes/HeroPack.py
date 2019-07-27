from Classes.Utils import Utils

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
    _heroList = [
        {
            'name': 'Anti-Mage',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Axe',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Batrider',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Bloodseeker',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Bounty Hunter',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Clockwerk',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Drow Ranger',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Enchantress',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Ogre Magi',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Shadow Shaman',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Tinker',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Tiny',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Tusk',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Warlock',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Beastmaster',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Chaos Knight',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Crystal Maiden',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Juggernaut',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Luna',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Morphling',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Nature\'s Prophet',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Puck',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Pudge',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Queen of Pain',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Slardar',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Timbersaw',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': True
        },
        {
            'name': 'Treant Protector',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Witch Doctor',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Abaddon',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Arc Warden',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Lina',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Lycan',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Omniknight',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Phantom Assassin',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Razor',
            'cost': 1,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Sand King',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Shadow Fiend',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Slark',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Sniper',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Terrorblade',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': True
        },
        {
            'name': 'Venomancer',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Viper',
            'cost': 3,
            'alliances': ('Elusive'),
            'hard': True
        },
        {
            'name': 'Windranger',
            'cost': 2,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Alchemist',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Disruptor',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Doom',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Dragon Knight',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Keeper of the Light',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Kunkka',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Lone Druid',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Medusa',
            'cost': 5,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Mirana',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Necrophos',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': True
        },
        {
            'name': 'Templar Assassin',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Troll Warlord',
            'cost': 5,
            'alliances': ('Elusive'),
            'hard': True
        },
        {
            'name': 'Enigma',
            'cost': 5,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Gyrocopter',
            'cost': 5,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Lich',
            'cost': 5,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Techies',
            'cost': 5,
            'alliances': ('Elusive'),
            'hard': False
        },
        {
            'name': 'Tidehunter',
            'cost': 4,
            'alliances': ('Elusive'),
            'hard': False
        }
    ]

    _heroIconFolder = ''

    def __init__(self, heroIconFolder):
        self._heroIconFolder = heroIconFolder
        self.count = 0

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
            if self.count < 1:
                func(Hero(heroDict['name'], heroDict['cost'], self._heroIconFolder, 1, heroDict['hard']))
                #self.count += 1

class HeroStorage:
    
    def __init__(self):
        self._storage = {}

    # All heroes are stored in tokens (1*)
    def store(self, hero, count = 0):
        heroName = hero.getName()
        heroDict = {}
        heroDict['hero'], heroDict['count'] = hero.tokenize()
        self._storage[heroName] = {'name': heroName, 'count': 0}
        if count != 0:
            self._storage[heroName]['count'] = count

        if heroName in self._storage:
            self._storage[heroName]['count'] += heroDict['count']
        else:
            self._storage[heroName] = heroDict

    def getHeroCount(self, heroName):
        try:
            return self._storage[heroName]['count']
        except:
            return 0

    def doWithEveryStoredHero(self, func):
        for hero in self._storage:
            func(hero)

