import cv2
import numpy as np

from PIL import Image, ImageDraw

from functools import partial
import pickle

from Classes.Utils import Utils
from Classes.Accountant import Accountant
from Classes.HeroPack import *

_backgroundColors = ('#25222d', '#312c40')
_starColors = ('#bbb2a9', '#b4c4e6', '#f3ef00')
_starColorsRgb = ((167, 168, 162), (180, 196, 230), (243, 250, 45))
#_starColorsRgb = ((37, 36, 41), (180, 196, 230), (52, 44, 59))

_tmpFolder = 'temp/'
_heroIconFolder = 'img/hero-icons/'
_levelIconFolder = 'img/scoreboard-icons/levels/'

_enableCache = 1

if __name__ == "__main__":
    oUtils = Utils(_tmpFolder, _levelIconFolder)
    oHeroFactory = HeroFactory(_heroIconFolder)

    playerS = HeroStorage()
    opponentS = HeroStorage()

    largeImgName = 'score5.png'
    resultImgName = 'result.png'

    largeImgNameCropped = oUtils.cropBig(largeImgName)
    large_image = cv2.imread(largeImgNameCropped)

    playerCrop, playerRow = oUtils.getPlayerCrop(largeImgName)
    playerLevel = oUtils.getPlayerLevel(playerCrop)
    print('Player row: %s \nPlayer level %s\n' % (playerRow, playerLevel)) 

    def findHeroOnImg(large_image, oHero):
        print('\nProcessing %s' % oHero.getName())

        smallImgName = oHero.getIcon() 
        small_image = cv2.imread(oUtils.cropSome(smallImgName))
        w, h = small_image.shape[:-1] # this lib is retarded, we have to swa:
        res = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)
        threshold = .6
        if oHero.hard:
            threshold = .5
        loc = np.where(res >= threshold)
        prevPts = []
        for pt in zip(*loc[::-1]):  # Switch collumns and rows
            if Utils.checkPointWithPrev(pt, prevPts):
                prevPts.append(pt)
                #cv2.rectangle(large_image, pt, (pt[0] + h, pt[1] + w), (0, 255, 0), 2)
                print("row: %s" % (pt,))
                try:
                    star = oUtils.getStarsByColor(largeImgNameCropped, (pt[0], pt[1], w, h), _starColorsRgb)
                    print(str(star) + ' stars\n')
                    foundList.append({'name': oHero.getName(), 'point': pt, 'star': star})
                except IndexError:
                    pass


    foundList = []
    try:
        cache = open('cache', 'r+b') 
        cacheData = cache.read()
    except IndexError:
        print('no cache!')
        cacheData = []
    if len(cacheData) and _enableCache:
        foundList = pickle.loads(cacheData)
    else:
        oHeroFactory.doWithEveryHero(partial(findHeroOnImg, large_image))
        pickler = pickle.Pickler(cache)
        pickler.dump(foundList)


    #filtering out bad finds
    largeH, largeW = large_image.shape[:-1]
    heroLineX = largeW / 16
    heroLineBenchX = largeW * .75
    heroLineBenchEndX = heroLineBenchX + 32 
    print(heroLineBenchX, heroLineBenchEndX)
    
    #finding start of hero lines
    heroLines = []
    for i, val in enumerate(foundList):
        pt = val['point']
        if pt[0] < heroLineX or (pt[0] > heroLineBenchX and pt[0] < heroLineBenchEndX):
            if pt[1] > playerRow[1] - largeH / 9  and pt[1] < playerRow[1] - largeH / 9 + playerRow[3]:
                val['player'] = True
            heroLines.append(val)
            del foundList[i]
    
    #If lines are close, they are in conflict !TODO solve conflict
    heroLines.sort(key=lambda k: k['point'][1])
    prev = 0
    conflicts = []
    for heroLine in heroLines:
        pt = heroLine['point']
        if prev != 0:
            if abs(pt[1] - prev[1]) < largeH / 10 and abs(pt[0] - prev[0]) < largeW / 2:
                conflicts.append((pt, prev))
        prev = pt 

    #Finding finds belonging to those lines
    for val in foundList:
        pt = val['point']
        for lineStart in heroLines:
            startPt = lineStart['point']
            if pt[0] > startPt[0] and abs(startPt[1] - pt[1]) < 5:
                heroLines.append(val)
                break
   
    
    for val in heroLines:
        pt = val['point']
        cv2.rectangle(large_image, pt, (pt[0] + 20, pt[1] + 20), (0, 255, 0), 2)
        hero = oHeroFactory.getHeroByName(val['name'], val['star'])
        try:
            val['player']
            playerS.store(hero)
        except KeyError:
            opponentS.store(hero)
    cv2.imwrite(resultImgName, large_image)

    oAccountant = Accountant(oHeroFactory, playerLevel, playerS, opponentS)




