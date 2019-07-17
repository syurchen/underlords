from Classes import Hero

class HeroFactory:
    #Should probably be in config
    _heroList = [
        {
            'name': 'Anti-Mage',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Axe',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Batrider',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Bloodseeker',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Bounty Hunter',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Clockwerk',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Drow Ranger',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Enchantress',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Ogre Magi',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Shadow Shaman',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Tinker',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Tiny',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Tusk',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Warlock hero',
            'cost': 1,
            'alliances': ('Elusive')
        },
        {
            'name': 'Beastmaster',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Chaos Knight',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Crystal Maiden',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Juggernaut',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Luna',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Morphling',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Nature\'s Prophet',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Puck',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Pudge',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Queen of Pain',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Slardar',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Timbersaw',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Treant Protector',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Witch Doctor',
            'cost': 2,
            'alliances': ('Elusive')
        },
        {
            'name': 'Abaddon',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Arc Warden',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Lina',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Lycan',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Omniknight',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Phantom Assassin',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Razor',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Sand King',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Shadow Fiend',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Slark',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Sniper',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Terrorblade',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Venomancer',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Viper',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Windranger',
            'cost': 3,
            'alliances': ('Elusive')
        },
        {
            'name': 'Alchemist',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Disruptor',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Doom',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Dragon Knight',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Keeper of the Light',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Kunkka',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Lone Druid',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Medusa',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Mirana',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Necrophos',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Templar Assassin',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Troll Warlord',
            'cost': 4,
            'alliances': ('Elusive')
        },
        {
            'name': 'Enigma',
            'cost': 5,
            'alliances': ('Elusive')
        },
        {
            'name': 'Gyrocopter',
            'cost': 5,
            'alliances': ('Elusive')
        },
        {
            'name': 'Lich',
            'cost': 5,
            'alliances': ('Elusive')
        },
        {
            'name': 'Techies',
            'cost': 5,
            'alliances': ('Elusive')
        },
        {
            'name': 'Tidehunter',
            'cost': 5,
            'alliances': ('Elusive')
        }
    ]

    _heroIconFolder = ''

    def __init__(self, heroIconFolder):
        self._heroIconFolder = heroIconFolder

    def doWithEveryHero(self, func):
        for heroDict in self._heroList:
            func(Hero(heroDict['name'], heroDict['cost'], self._heroIconFolder))

