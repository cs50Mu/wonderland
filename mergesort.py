#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'


def merge(L1,L2):
    """Merge sorted lists L1 and L2 and return the result."""
    mergedlist = []
    i1 = i2 = 0
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            mergedlist.append(L1[i1])
            i1 += 1
        else:
            mergedlist.append(L2[i2])
            i2 += 1

    mergedlist.extend(L1[i1:])
    mergedlist.extend(L2[i2:])
    return mergedlist
            
def mergesort(L):
    """Sort L."""

    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])

    count = 0
    while count < len(workspace)-1:
        newList = merge(workspace[count],workspace[count+1])
        print newList
        workspace.append(newList)
        count += 2

    return workspace[-1][:]


if __name__=="__main__":
#    print merge([6,7,8,9],[1,3,5])
    print mergesort([9,8,7,6,5,4,3,2,1,0])
