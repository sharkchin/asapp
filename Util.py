__author__ = 'axia'

negFilePath = 'rt-polaritydata/rt-polarity.neg'
negFileRowCnt = 5331
posFilePath = 'rt-polaritydata/rt-polarity.pos'
posFileRowCnt = 5331

def getStopWords(filePathArr, minCount):
    wordMap = {}
    for filePath in filePathArr:
        with open(filePath, 'r') as f:
            for line in f:
                for word in line.split():
                    word = word.lower()
                    if(word in wordMap):
                        wordMap[word] += 1
                    else:
                        wordMap[word] = 1
    for word, freq in list(wordMap.items()):
        if(freq < minCount):
            del wordMap[word]
    return wordMap

def stopWords(minCount):
    return getStopWords([negFilePath,posFilePath],minCount)


print(stopWords(100))