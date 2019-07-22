import cv2
import numpy as np

from PIL import Image, ImageDraw

from functools import partial

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

if __name__ == "__main__":
    oUtils = Utils(_tmpFolder, _levelIconFolder)
    oHeroFactory = HeroFactory(_heroIconFolder)

    playerStorage = HeroStorage()
    oppStorage = HeroStorage()

    largeImgName = 'score4.png'
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
                cv2.rectangle(large_image, pt, (pt[0] + h, pt[1] + w), (0, 255, 0), 2)
                print("row: %s" % (pt,))
                try:
                    print(str(oUtils.getStarsByColor(largeImgNameCropped, (pt[0], pt[1], w, h), _starColorsRgb)) + ' stars\n')
                except IndexError:
                    pass

        cv2.imwrite(resultImgName, large_image)


    oHeroFactory.doWithEveryHero(partial(findHeroOnImg, large_image))








