import os, fnmatch, ntpath, re
from PIL import Image
import numpy as np
import cv2
import hashlib
import time

class Utils:
    def __init__(self, tmpFolder, levelIconFolder):
        self._tmpFolder = tmpFolder
        self._levelIconFolder = levelIconFolder

    def OsFind(pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    return os.path.join(root, name)
        print(pattern, result)
        return result

    def addBackground(self, imgName, colorHex):
        img = Image.open(imgName)
        webhexcolor = colorHex
        w, h = img.size
        bgImg = Image.new("RGB", (w - 1, h - 1), webhexcolor)

        bgImg.paste(img, (0, 0, h, w), img)
        filename = self._tmpFolder + ntpath.basename(imgName) + colorHex + '.png'
        bgImg.save(filename)
        bgImg.close()
        return filename

# Removing side part from Icon
    def cropSome(self, imgName):
        filename = self._tmpFolder + ntpath.basename(imgName) + '-cropped.png'
        if os.path.isfile(filename):
            return filename

        img = Image.open(imgName)
        w, h = img.size
        left = w / 4
        top = h / 4
        right = 3 * w / 4
        bottom = 3 * h / 4
        cropped = img.crop((left, top, right, bottom))
        cropped.save(filename)
        cropped.close()
        os.system('./pngcrush -ow -rem allb -reduce %s' % filename)
        return filename

    def cropBig(self, imgName):
        filename = self._tmpFolder + ntpath.basename(imgName) + '-cropped.png'
        if os.path.isfile(filename):
            return filename

        img = Image.open(imgName)
        w, h = img.size
        left = w / 4
        top = h / 16
        right = 13.8 * w / 16
        bottom =  14.2 * h / 16
        cropped = img.crop((left, top, right, bottom))
        Utils.changeContrast(cropped, 254)
        cropped.save(filename)
        cropped.close()
        os.system('./pngcrush -ow -rem allb -reduce %s' % filename)
        return filename


# Returns our player pic **hopefully**
    def getPlayerCrop(self, filename):
        img = cv2.imread(filename)

        img_final = cv2.imread(filename)
        img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
        image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
        ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        dilated = cv2.dilate(new_img, kernel, iterations=9)

        contours, hierarchy = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # findContours returns 3 variables for getting contours
        
        fullW, fullH, _ = img_final.shape
        largest = (0, 0, 0, 0)
        for contour in contours:
            # get rectangle bounding contour
            [x, y, w, h] = cv2.boundingRect(contour)

            # Don't plot small false positives that aren't text
            if w < 15 and h < 15 or x > fullW / 8:
                continue
            
            if largest[3] * largest[2] < w * h:
                largest = (x, y, w, h)
        
        x, y, w, h = largest
        '''
        cv2.rectangle(img, (0, y), (round(fullW / 8), y + h), (255, 0, 255), 2)
        cv2.imwrite('result.png', img)
        '''

        cropped = img_final[y :y +  h , 0 : round(fullW / 8)]

        s = self._tmpFolder + ntpath.basename(filename) + '-player-cropped.png'
        cv2.imwrite(s , cropped)

        return s, largest

# Takes player pic, returns lvl as int
    def getPlayerLevel(self, imgName):
        large_image = cv2.imread(imgName)


        for (_, _, filenames) in os.walk(self._levelIconFolder):
            for filename in filenames:
                small_image = cv2.imread(self._levelIconFolder + filename)
                w, h = small_image.shape[:-1]

                res = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)
                threshold = .8
                loc = np.where(res >= threshold)
                if loc[0].size > 0:
                    return int(re.findall('\d+', filename)[0])

    def changeContrast(img, level):
        factor = (259 * (level + 255)) / (255 * (259 - level))
        def contrast(c):
            return 128 + factor * (c - 128)
        return img.point(contrast)


    def getStarsByColor(self, bigImgName, frame, starColorsRgb, tryNext = 0):
        img = Image.open(bigImgName).convert("RGBA")
        Utils.changeContrast(img, 254)
        loaded = img.load()

        x, y, w, h = frame
        pixel = (int(x + round(w / 2)) + tryNext, int(y + round(h * 1.6)))
        r, g, b, a  = loaded[pixel[0], pixel[1]]

        img.close()

        #print('RGB: %s\nPixel: %s' % ((r, g, b, a), pixel))
        for rgb in starColorsRgb:
            delta = abs(rgb[0] - r) / 3 + abs(rgb[1] - g) / 2 + abs(rgb[2] - b)
            if delta < 50:
                return starColorsRgb.index(rgb) + 1
            #print('Delta %s: %s' % (starColorsRgb.index(rgb) + 1, delta))
        
        if tryNext == 0:
            self.getStarsByColor(bigImgName, frame, starColorsRgb, -5)

        # its likely that we hit between 2 stars 
        return 2

    def checkPointWithPrev(pt, prevPts):
        for prev in prevPts:
            if abs(prev[0] - pt[0]) < 10 and  abs(prev[1] - pt[1]) < 10:
                return False
        return True

    def createNewAndOldRandomFilename(oldName):
        ext = os.path.splitext(oldName)[1]
        noExt = os.path.splitext(oldName)[0]
        m = hashlib.md5()
        m.update(oldName.encode('utf-8'))
        m.update(str(time.time()).encode('utf-8'))
        hashed = str(m.hexdigest())
        return  hashed + ext, noExt + '-' + hashed + ext

    def getRealOldFilename(oldName):
        splitMinus = oldName.split('-')
        ext = os.path.splitext(oldName)[1]
        return ''.join(splitMinus[:-1]) + ext

    def prepareHeroName(oldName):
        pronouns = ['of', 'the']
        exceptions = {'antimage': 'Anti-Mage',
                      'bat_rider': 'Batrider',
                      'furion': 'Nature\'s Prophet',
                      'wind_ranger': 'Windranger'}

        try:
            return exceptions[oldName]
        except KeyError:
            pass

        oldName = oldName.split('_')
        result = ''
        for part in oldName:
            if part not in pronouns:
                part = part.capitalize() 
            result += part + ' '
        return result[:-1]
