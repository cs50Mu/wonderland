#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

from Tkinter import *

window = Tk()

frame = Frame(window)
frame.pack()

var = StringVar()

label = Label(frame,textvariable=var)
label.pack()

entry = Entry(frame,textvariable=var)
entry.pack()

window.mainloop()
