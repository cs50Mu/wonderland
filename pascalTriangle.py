#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified:09/19/2013 

"""the method to form a line of the triangle is this:
    given one line,add a '0' to its head and end seperately 
    to form two new lines,then add them together digit by digit,
    the new-formed line is the next line
    to-do: 格式化输出
"""

__revision__ = '0.1'

height = int(raw_input("Please enter the height of the triangle: "))
l = [1,]
for i in range(height):
    print l
    this = [0,] + l
    that = l + [0,]
    l = [ x+y for (x,y) in zip(this,that) ]
