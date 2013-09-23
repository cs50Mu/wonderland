#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified:07/04/2013 

"""Merge sort,recursion version
"""

__revision__ = '0.1'


def merge(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



def mergesort(L):
    if len(L) <= 1:    # Base case
        return L
    else:
        middle = int(len(L)/2)
        left = mergesort(L[:middle])  # merge left side first
        right = mergesort(L[middle:]) # then merge right side
        return merge(left,right)   # finally merge the two sides

print mergesort([9,8,7,6,5,4,3,2,1,0])
