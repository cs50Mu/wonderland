#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import re
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')  # notice here
r = requests.get('http://www.weather.com.cn/textFC/hb.shtml')
#with open('weather.html','w') as f:
#    f.write(r.text)
issuetime = (re.findall(r'<dt>\s+(.+?)\s+<span',r.text,flags=re.S))[0]
TJtable = (re.findall(r'<table\s+.+?</table>',r.text,flags=re.S))[1]
TJtr = (re.findall(r'<tr>.+?</tr>',TJtable,flags=re.S))[2]
sky = (re.findall(r'<td width="82">(.+?)</td>',TJtr,flags=re.S))[0]
wind = (re.findall(r'<td width="168"><span>(.+?)</span><span class="conMidtabright">(.+?)</span>',TJtr,flags=re.S))[0]
temperature = (re.findall(r'<td width="86">(.+?)</td>',TJtr,flags=re.S))[0]
print '%s,今天天气%s,%s,%s,气温%s\nHave a NICE day!' %(issuetime,sky,wind[0],wind[1],temperature)

