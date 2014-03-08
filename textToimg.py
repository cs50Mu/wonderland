#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import Image,ImageFont,ImageDraw

text1 = u'你好，pygame！'
im = Image.new("RGB",(300,50),(255,255,255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype('ZhunYuan.ttf',24)
dr.text((10,5),text1,font=font,fill="#000000")
im.show()
