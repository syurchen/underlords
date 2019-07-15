import cv2
import pytesseract
import numpy as np
import os, fnmatch, ntpath, re

from PIL import Image

_backgroundColors = ['#25222d', '#312c40']

_tmpFolder = 'temp/'
_heroIconFolder = 'img/hero-icons/'
_levelIconFolder = 'img/scoreboard-icons/levels/'

def OsFind(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return os.path.join(root, name)
                #result.append(os.path.join(root, name))
    return result


def addBackground(imgName, colorHex):
    img = Image.open(imgName)
    webhexcolor = colorHex
    w, h = img.size
    bgImg = Image.new("RGB", (w - 1, h - 1), webhexcolor)

    bgImg.paste(img, (0, 0, h, w), img)
    filename = _tmpFolder + ntpath.basename(imgName) + colorHex + '.png'
    bgImg.save(filename)
    bgImg.close()
    return filename

# Removing side part
def cropSome(imgName):
    img = Image.open(imgName)
    w, h = img.size
    left = w / 4
    top = h / 4
    right = 3 * w / 4
    bottom = 3 * h / 4
    cropped = img.crop((left, top, right, bottom))
    filename = _tmpFolder + ntpath.basename(imgName) + '-cropped.png'
    cropped.save(filename)
    cropped.close()
    return filename

# Returns our player pic **hopefully**
def getPlayerCrop(file_name):
    img = cv2.imread(file_name)

    img_final = cv2.imread(file_name)
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
            print(largest)
    
    x, y, w, h = largest
    cv2.rectangle(img, (0, y), (round(fullW / 8), y + h), (255, 0, 255), 2)
    cv2.imwrite('result.png', img)

    cropped = img_final[y :y +  h , 0 : round(fullW / 8)]

    s = _tmpFolder + ntpath.basename(file_name) + '-cropped.png'
    cv2.imwrite(s , cropped)

    # write original image with added contours to disk

    return s

# Takes player pic, returns lvl as int
def getPlayerLevel(imgName):
    large_image = cv2.imread(imgName)


    for (_, _, filenames) in os.walk(_levelIconFolder):
        for filename in filenames:
            small_image = cv2.imread(_levelIconFolder + filename)
            w, h = small_image.shape[:-1]

            res = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)
            threshold = .6
            loc = np.where(res >= threshold)
            if loc[0].size > 0:
                return re.findall('\d+', filename)[0]

if __name__ == "__main__":
    method = cv2.TM_SQDIFF
    smallImgName = OsFind('Axe*', _heroIconFolder)
    
    small_image = cv2.imread(cropSome(smallImgName))
    #large_image = cv2.imread('score.png')
    large_image = cv2.imread('score3.jpg')
    #large_image = cv2.imread('score2.jpeg')

    w, h = small_image.shape[:-1]

    res = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)
    threshold = .6
    loc = np.where(res >= threshold)
    prev = 0
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        if prev == 0:
            prev = pt
        else:
            if abs(prev[0] - pt[0]) < 10 and  abs(prev[1] - pt[1]) < 10:
                continue
            else:
                prev = pt
        cv2.rectangle(large_image, pt, (pt[0] + h, pt[1] + w), (0, 255, 0), 2)
        print("row:")
        print(pt)

    cv2.imwrite('result.png', large_image)

    getPlayerLevel(getPlayerCrop('result.png'))




