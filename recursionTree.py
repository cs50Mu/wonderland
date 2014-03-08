#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""理解的关键是，要知道在一个函数递归
调用结束（即达到递归调用的基本条件）后会继续
执行后续的代码，函数套函数来调用，确实
比较混乱。
"""

__revision__ = '0.1'

from turtle import *

def branch(length,level):
    if level <= 0:
        return
    forward(length)
    left(45)
    branch(0.6*length,level-1)
    right(90)
    branch(0.6*length,level-1)
    left(45)
    backward(length)
    return

left(90)
branch(100,5)
