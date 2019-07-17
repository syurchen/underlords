import os

class Utils:

    _heroList = [
        [
            'name': 'Anti-Mage',
            'cost': 1,
            'alliances': ('Elusive')
        ],
        [
            'name': 'Axe',
            'cost': 1,
            'alliances': ('Elusive')
        ],
        [
            'name': 'Batrider',
            'cost': 1,
            'alliances': ('Elusive')
        ],
Bloodseeker
Bounty Hunter
Clockwerk
Drow Ranger
Enchantress
Ogre Magi
Shadow Shaman
Tinker
Tiny
Tusk
Warlock hero
Beastmaster
Chaos Knight
Crystal Maiden
Juggernaut
Luna
Morphling
Nature&#39;s Prophet
Puck
Pudge
Queen of Pain
Slardar
Timbersaw
Treant Protector
Witch Doctor
Abaddon
Arc Warden
Lina
Lycan
Omniknight
Phantom Assassin
Razor
Sand King
Shadow Fiend
Slark
Sniper
Terrorblade
Venomancer
Viper
Windranger
Alchemist
Disruptor
Doom
Dragon Knight
Keeper of the Light
Kunkka
Lone Druid
Medusa
Mirana
Necrophos
Templar Assassin
Troll Warlord
Enigma
Gyrocopter
Lich
Techies
Tidehunter

    def OsFind(pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    return os.path.join(root, name)
        return result
