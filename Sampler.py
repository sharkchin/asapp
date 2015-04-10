__author__ = 'axia'
import random

negFilePath = 'rt-polaritydata/rt-polarity.neg'
negFileRowCnt = 5331
posFilePath = 'rt-polaritydata/rt-polarity.pos'
posFileRowCnt = 5331

def len(filePath):
    return sum(1 for line in open(filePath))

#print(len(posFilePath))

def getSample(filePath, cnt):
    with open(filePath) as f:
        rows = f.readlines()
        return random.sample(rows,cnt)

#for item in getSample(negFilePath,3):
#    print(item)

def getPosSample(cnt):
    return getSample(posFilePath,cnt)

def getNegSample(cnt):
    return getSample(negFilePath,cnt)