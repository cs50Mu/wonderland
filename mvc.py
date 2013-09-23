#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

from Tkinter import *
def click(var,value):
    counter.set(var.get()+value)

if __name__ == '__main__':
    window = Tk()
    counter = IntVar()
    counter.set(0)
    frame = Frame(window)
    frame.pack()

    button = Button(frame,text="Up",command=lambda: click(counter,1))
    button.pack()
    button = Button(frame,text="Down",command=lambda: click(counter,-1))
    button.pack()


    label = Label(frame,textvariable=counter)
    label.pack()

    window.mainloop()
