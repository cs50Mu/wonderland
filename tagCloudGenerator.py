#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""generate a tag cloud from
a given article
"""

__revision__ = '0.1'

import string

def readLine(dataFile):
    lineList = []
    with open(dataFile,'r') as f:
        for line in f:
            if line == '\n':
                continue
            wordList = line.strip().split()
            for word in wordList:
                if word  not in string.punctuation:  # skip punctuation like '-'
                    word = word.lower().strip(string.punctuation) # strip punctuations
                    lineList.append(word)
        return lineList

#print readLine('data/gettysburg.txt')
def stopWordlist(dataFile):
    stopWordlist = []
    with open(dataFile,'r') as f:
        for line in f:
            stopWordlist.append(line.strip().lower())
        return stopWordlist

def addWord(lineList,Dict):
    for word in lineList:
        if word in Dict:
            Dict[word] += 1
        else:
            Dict[word] = 1
    return Dict

def prettyPrint(Dict):
    print '\nThere are %d words in this article\n' %(len(Dict))
    print '-' * 40
    dictList = [ (value,key) for key,value in Dict.items()]
    dictList.sort(reverse=True)
    for value,key in dictList:
        if value > 2 and len(key) > 3 and key not in stopWordlist:
            print "%20s%20d" %(key,value)


def generateTag(Dict):
    tagString = ''
    count = 0
    for key,value in Dict.items():
        if value >2 and len(key) >3 and key not in stopWordlist:
            count += 1
            tagString += '<span style=\"font-size:%dpx;\">%s</span>' %(value*10,key+' ')
            if count % 5 == 0:
                tagString += '<br />'
    with open('tagCloud.html','w') as f:
        htmlString = "<html>\n<head><title>Tag Cloud</title></head>\n\n<body>\n<div align=\"center\">%s</div></body>\n</html>" %tagString
#        htmlString = "<html>\n<head><title>Tag Cloud</title></head>\n\n<body>\n%s</body>\n</html>" %tagString
        f.write(htmlString)


Dict = {}
stopWordlist = stopWordlist('stopword.txt')
#prettyPrint(addWord(readLine('data/gettysburg.txt'),Dict))
#prettyPrint(addWord(readLine('economist01.txt'),Dict))
generateTag(addWord(readLine('economist.txt'),Dict))
#generateTag(addWord(readLine('data/gettysburg.txt'),Dict))
#generateTag(addWord(readLine('Declaration of Independence'),Dict))

