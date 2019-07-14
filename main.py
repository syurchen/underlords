import cv2
import numpy as np
import os, fnmatch, ntpath

from PIL import Image

backgroundColors = ['#25222d', '#312c40']

tmpFolder = 'temp/'
heroIconFolder = 'img/hero-icons/'

def OsFind(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return os.path.join(root, name)
                #result.append(os.path.join(root, name))
    return result


def addBackground(imgName, colorHex):
    return imgName
    img = Image.open(imgName)
    webhexcolor = colorHex
    w, h = img.size
    bgImg = Image.new("RGB", (w - 1, h - 1), webhexcolor)

    bgImg.paste(img, (0, 0, h, w), img)
    filename = tmpFolder + ntpath.basename(imgName) + colorHex + '.png'
    bgImg.save(filename)
    bgImg.close()
    return filename

# Removing bottom part in case stars are there
def cropSome(imgName):
    img = Image.open(imgName)
    w, h = img.size
    left = w / 4
    top = h / 4
    right = 3 * w / 4
    bottom = 3 * h / 4
    cropped = img.crop((left, top, right, bottom))
    filename = tmpFolder + ntpath.basename(imgName) + '-cropped.png'
    cropped.save(filename)
    cropped.close()
    return filename

if __name__ == "__main__":
    method = cv2.TM_SQDIFF
    smallImgName = OsFind('Blood*', heroIconFolder)
    
    small_image = cv2.imread(cropSome(addBackground(smallImgName, backgroundColors[1])))
    #small_image = cv2.imread(tmpFolder + 'ogre.png')
    large_image = cv2.imread('score.png')

    w, h = small_image.shape[:-1]

    res = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)
    threshold = .7
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


