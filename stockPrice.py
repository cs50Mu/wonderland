#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""find the best and the worst monthly average
stock price for google.For me the dificult 
part is how to identify each week since the 
price is stored in a daily form
"""

__revision__ = '0.1'

def getDataList(filename):
    dataList = []
    with open(filename,'r') as f:
        next(f)  # skip the first line
        for line in f:
            dataList.append(line.strip().split(','))
    return dataList

def getMonthlyAverages(dataList):
    monthlyAveragesList = []
    monthYear = dataList[0][0][0:7]
    productSum = 0
    volumeSum = 0
#    print monthYear
    for day in dataList:
        if day[0][0:7] == monthYear:
            product = float(day[5]) * float(day[6])
            productSum += product
            volumeSum += float(day[6])
        else:
            averagePrice = productSum/volumeSum
            monthlyAveragesList.append((averagePrice,monthYear))
            monthYear = day[0][0:7]
            productSum = 0
            volumeSum = 0
            product = float(day[5]) * float(day[6])
            productSum += product
            volumeSum += float(day[6])

    averagePrice = productSum/volumeSum
    monthlyAveragesList.append((averagePrice,monthYear))
    return monthlyAveragesList

def printInfo(monthlyAveragesList):
    monthlyAveragesList.sort(reverse=True)
    print '*'*10,'The Top 6 Prices','*'*10
    print "%10s%20s" %('Date','Price')
    best = monthlyAveragesList[0:6]
    last = monthlyAveragesList[-6:]
    for x,y in best:
        print "%10s%20.2f" %(y,x)
    print '*'*10,'The Worst 6 Prices','*'*10
    for x,y in last:
        print "%10s%20.2f" %(y,x)

#    print monthlyAveragesList
#    print monthlyAveragesList[0:7]
#    print '\n\n'
#    print monthlyAveragesList[-6:]

printInfo(getMonthlyAverages(getDataList('data/table.csv')))
