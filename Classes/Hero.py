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
            # @TODO
            return self._iconPath
    
    def getIcon(self):
        return self._iconPath

    def getCost(self):
        return self._cost

    def getStar(self):
        return self._star

    def tokenize(self):
        count = self._star
        self._star = 1
        return count



