#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""create a messy document from a
well-ordered document.The specific
method used is this:keep the first
and the last letter unchanged,shuffle
the letters between them, notice
that it can also handle the punctuations
properly
"""

__revision__ = '0.1'

import random
import string

# create wordlist from text file
with open('data/gettysburg.txt','r') as f:
    wordList = []
    for line in f:
        if line == '\n':
            wordList.extend('\n\n')
        wordList.extend(line.split())

# make new wordlist
newWordList = []
for word in wordList:
    punct = ''
    if word[-1] in string.punctuation:
        punct = word[-1]
        word = word[:-1]
    if len(word) >= 4:
        l = list(word[1:len(word)-1])
        random.shuffle(l)
        newWord = word[0] + ''.join(l) + word[-1] + punct
        newWordList.append(newWord)
    else:
        newWordList.append(word+punct)

# list to string
print ' '.join(newWordList)

