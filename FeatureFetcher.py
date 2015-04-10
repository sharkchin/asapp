__author__ = 'axia'

from collections import Counter
from Sampler import getNegSample
from Sampler import getPosSample
import operator

sampleSize = 10
posSample = getPosSample(sampleSize)
negSample = getNegSample(sampleSize)

def sortedWordMap(sample):
    dict = Counter(' '.join(sample).split(' '))
    return [(k, v) for v, k in sorted(
        [(v, k) for k, v in dict.items()], reverse=True
    )]

posMap = sortedWordMap(posSample)
negMap = sortedWordMap(negSample)

def filterList(posMap, negMap)
    intersectSet = set()
    for pos in posMap:
        for neg in negMap:
            if(pos[0] == neg[0]):
                intersectSet.add(pos[0])
    for pos in posMap:
        if(pos[0] in intersectSet):


# for item in negMap:
#     print(item)
