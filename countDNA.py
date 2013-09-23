#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

from Tkinter import *

window = Tk()

A = IntVar()
T = IntVar()
C = IntVar()
G = IntVar()
result = StringVar()
def getNum(text):
   data = text.get('0.0',END)
   result.set('Num As: %d Num Ts: %d Num Cs: %d Num Gs: %d' \
           %(data.count('A'),\
           data.count('T'),\
           data.count('C'),\
           data.count('G')))

text = Text(window)
text.pack()
button = Button(window,text="Count",command=lambda: getNum(text))
button.pack()
label = Label(window,textvariable=result)
label.pack()

window.mainloop()
