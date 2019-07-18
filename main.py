import cv2
import numpy as np

from PIL import Image, ImageDraw

from Classes.Utils import Utils
from Classes.HeroPack import *

_backgroundColors = ('#25222d', '#312c40')
_starColors = ('#bbb2a9', '#b4c4e6', '#f3ef00')
_starColorsRgb = ((167, 168, 162), (180, 196, 230), (243, 250, 45))

_tmpFolder = 'temp/'
_heroIconFolder = 'img/hero-icons/'
_levelIconFolder = 'img/scoreboard-icons/levels/'

if __name__ == "__main__":
    Utils = Utils(_tmpFolder, _levelIconFolder)
    method = cv2.TM_SQDIFF
    smallImgName = Utils.OsFind('Tink*', _heroIconFolder)

    largeImgName = 'score4.png'
    
    small_image = cv2.imread(Utils.cropSome(smallImgName))
    large_image = cv2.imread(largeImgName)

    w, h = small_image.shape[:-1]

    res = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)
    threshold = .6
    loc = np.where(res >= threshold)
    prevPts = []
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        if Utils.checkPointWithPrev(pt, prevPts):
            prevPts.append(pt)
            cv2.rectangle(large_image, pt, (pt[0] + h, pt[1] + w), (0, 255, 0), 2)
            print("row:")
            print(pt)
            print(str(Utils.getStarsByColor(largeImgName, (pt[0], pt[1], w, h), _starColorsRgb)) + ' stars')

    cv2.imwrite('result.png', large_image)

    Utils.getPlayerLevel(Utils.getPlayerCrop('result.png'))




