from Classes import Utils 

class Hero:
    _name = ''
    _cost = 1
    _star = 1

    _iconPath = ''
    _iconFolder = ''

    def __init__(self, name, cost, iconFolder, star = 1):
        self._name = name
        self._cost = cost
        self._star = star
        self._iconFolder = iconFolder

    def findIcon(self):
        if self._iconPath != '':
            return self._iconPath
        else:
            self._iconPath = Utils.OsFind(self._name, self._iconFolder) 
            return self._iconPath

    def getName(self):
        return self._name

    def getIcon(self):
        return self._iconPath

    def getCost(self):
        return self._cost

    def getStar(self):
        return self._star

    def tokenize(self):
        count = 3 ** (self._star - 1)
        self._star = 1
        return count



