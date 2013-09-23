#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

def getDataList(filename):
    dataList = []
    with open(filename,'r') as f:
        next(f)  # skip the first line
        for line in f:
            dataList.append(line.strip().split(','))
    return dataList
def getEfficiencyList(dataList):
    efficiencyList = []
    for player in dataList:
        for i in xrange(len(player)):
            if player[i].isdigit():
                player[i] = int(player[i])
            elif player[i] == 'NULL':
                player[i] = 0
#    print dataList
    for player in dataList:
#        print player
        efficiency = ((player[8]+player[11]+player[12]+\
                player[13]+player[14])-((player[17]-\
                player[18])+(player[19]-player[20])+\
                player[15]))/player[6]
        name = player[2] + ' ' + player[3]
        year = player[1]
        efficiencyList.append((efficiency,name,year))

    return efficiencyList
def printInfo(efficiencyList):
    efficiencyList.sort(reverse=True)
    print '*'*30 + 'The Top 50 Players' + '*'*30
    print '%20s%20s%40s' %('Name','Year','Efficiency')
    for player in efficiencyList[:50]:
        print '%20s%20s%40d' %(player[1],player[2],player[0])
printInfo(getEfficiencyList(getDataList('data/player_regular_season.csv')))
