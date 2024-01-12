import cv2
import os
import sys
import numpy as np
from time import strftime, localtime

assetFolder='tgscc/'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: solve.py <targetImageFile>")
        exit(1)

    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))

    targetFilename = sys.argv[1]
    targetImage = cv2.imread(targetFilename)[0:300]
    detectCharLength = targetImage.shape[1] // 300

    print("detectCharLength:", detectCharLength)
    resultArray = []

    targetSplit = np.split(targetImage, detectCharLength, axis=1)

    for i in range(detectCharLength):
        for x in range(0, 300):
            targetSplit[i][x][0] = [255, 255, 255]
            targetSplit[i][x][299] = [255, 255, 255]
        for y in range(0, 300):
            targetSplit[i][0][y] = [255, 255, 255]
            targetSplit[i][299][y] = [255, 255, 255]

    filelist = os.listdir(assetFolder)

    for i in range(detectCharLength):
        minDifference = 1073741824
        minChar = ''
        for filename in filelist:
            image = cv2.imread(f"{assetFolder}{filename}")
            difference = 1-np.equal(targetSplit[i], image).mean()
            if difference < minDifference:
                minDifference = difference
                minChar = filename[:4]
        print(chr(int(minChar,16)), " diff:", minDifference)
        resultArray.append(chr(int(minChar,16)))
    print("".join(resultArray))

    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
