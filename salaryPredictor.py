#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

def makeDataSet(dataFile):
    dataList = []
    with open(dataFile) as f:
        for line in f:
            if '?' in line:
                continue
            age,workclass,fnlwgt,edu,eduNum,marital,occupation,relationship,\
                    race,sex,capitalGain,capitalLoss,hours,country,salary = line.strip().split(',')
            if salary == ' <=50K' or salary == ' <=50K.':
                salary = 0
            else:
                salary = 1
            adultTuple = (salary,int(age),int(eduNum),int(capitalGain),int(capitalLoss),int(hours),workclass,marital,occupation,relationship,\
                    race,sex)
            dataList.append(adultTuple)
    return dataList

#print makeDataSet('adult.data')[:50]

def sumLists(list1,list2):
    sumList = [0] * 5
    for i in range(5):
        sumList[i] = list1[i] + list2[i]
    return sumList

def makeAverage(sumList,total):
    averageList = [0] * 5
    for i in range(5):
        averageList[i] = sumList[i]/float(total)
    return averageList

def updateDicts(dataList,dictList):
    for data,dictionary in zip(dataList,dictList):
        if data not in dictionary:
            dictionary[data] = 1
        else:
            dictionary[data] += 1

def maxDict(dictList):
    maxList = []
    for dictionary in dictList:
        L = [ (value,key) for key,value in dictionary.items() ]
        L.sort(reverse = True)
        maxList.append(L)
    return maxList


def trainClassifier(dataList):
    workclassR = {} 
    workclassP = {}
    maritalR = {}
    maritalP = {}
    occupationR ={}
    occupationP = {}
    relationshipR = {}
    relationshipP = {}
    raceR = {}
    raceP = {}
    sexR = {}
    sexP ={}
    rich = [0] * 5
    poor = [0] * 5
    richCount = 0
    poorCount = 0
    for p in dataList:
        if p[0] == 0:
            poor = sumLists(poor,p[1:6])
            updateDicts(p[6:],[workclassP,maritalP,occupationP,relationshipP,raceP,sexP])
            poorCount += 1
        else:
#            print p
            rich = sumLists(rich,p[1:6])
            updateDicts(p[6:],[workclassR,maritalR,occupationR,relationshipR,raceR,sexR])
            richCount += 1
    
#    print workclassR
#    print workclassP
    poorAverage = makeAverage(poor,poorCount)
    richAverage = makeAverage(rich,richCount)
    poorMaxList = maxDict([workclassP,maritalP,occupationP,relationshipP,raceP,sexP])
    richMaxList = maxDict([workclassR,maritalR,occupationR,relationshipR,raceR,sexR])
    poorClassifier = []
    richClassifier = []
    for i in range(4):
        for j in range(len(poorMaxList[i])):
            if poorMaxList[i][j][1] != richMaxList[i][j][1]:
                poorClassifier.append(poorMaxList[i][j][1])
                richClassifier.append(richMaxList[i][j][1])
                break
    classifier = makeAverage(sumLists(poorAverage,richAverage),2),poorClassifier,richClassifier
#    print poorAverage
#    print richAverage
    return classifier

#for item in trainClassifier(makeDataSet('adult.data')):
#    print item

def classifyTestSet(testSet,classifier):
    results = []
    for p in testSet:
        poor = 0
        rich = 0
        for i in range(len(p[1:6])):
            if p[i+1] > classifier[0][i]:
                rich += 1
            else:
                poor += 1
        for j in range(len(p[6:10])):
            if p[j+6] == classifier[1]:
                poor += 1
            elif p[j+6] == classifier[2]:
                rich += 1
        resultTuple = p[0],poor,rich
        results.append(resultTuple)
    return results


def reportResults(results):
    totalCount = 0
    incorrect = 0
    for result in results:
        totalCount += 1
        if result[1] > result[2]:
            if result[0] == 1:
                incorrect += 1
        elif result[0] == 0:
            incorrect += 1

    print 'Of ',totalCount,' people, there were ',incorrect,' incorrects'
    print 'There are %' + str(incorrect*100/float(totalCount)) + ' incorrects'


reportResults(classifyTestSet(makeDataSet('adult.test'),trainClassifier(makeDataSet('adult.data'))))
