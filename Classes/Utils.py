import os, fnmatch, ntpath, re
from PIL import Image, ImageDraw
import numpy as np
import cv2

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
        return result


    def addBackground(self, imgName, colorHex):
        img = Image.open(imgName)
        webhexcolor = colorHex
        w, h = img.size
        bgImg = Image.new("RGB", (w - 1, h - 1), webhexcolor)

        bgImg.paste(img, (0, 0, h, w), img)
        filename = _tmpFolder + ntpath.basename(imgName) + colorHex + '.png'
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
        return filename

    def cropBig(self, imgName):
        filename = self._tmpFolder + ntpath.basename(imgName) + '-cropped.png'
        if os.path.isfile(filename) and 0:
            return filename

        img = Image.open(imgName)
        w, h = img.size
        left = w / 4
        top = h / 16
        right = 14.5 * w / 16
        bottom =  14.2 * h / 16
        cropped = img.crop((left, top, right, bottom))
        cropped.save(filename)
        cropped.close()
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
                threshold = .6
                loc = np.where(res >= threshold)
                if loc[0].size > 0:
                    return re.findall('\d+', filename)[0]

    def getStarsByColor(self, bigImgName, frame, starColorsRgb):
        img = Image.open(bigImgName)
        rgb_img = img.convert('RGB')
        x, y, w, h = frame

        pixel = (int(x + round(w / 2)), int(y + round(h * 1.6)))
        r, g, b = rgb_img.getpixel(pixel)

        img.close()
        rgb_img.close()

        print((r, g, b))
        print(pixel)
        for rgb in starColorsRgb:
            delta = abs(rgb[0] - r) / 3 + abs(rgb[1] - g) / 2 + abs(rgb[2] - b)
            if delta < 70:
                return starColorsRgb.index(rgb) + 1
            print(delta)
        
        # its likely that we hit between 2 stars 
        return 2

    def checkPointWithPrev(pt, prevPts):
        for prev in prevPts:
            if abs(prev[0] - pt[0]) < 10 and  abs(prev[1] - pt[1]) < 10:
                return False
        return True

    def checkPointWithDeadZone(pt, bigShape):
        return True

