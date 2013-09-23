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
r = requests.get('http://wap.weather.com.cn/wap/weather/101030100.shtml')
with open('weather.html','w') as f:
    f.write(r.text)
issuetime = re.findall(r'<h3>(.+?)</h3>',r.text)
time = re.findall(r'<dd>(.+?)<br',r.text)
weather = re.findall(r'<dt>(.+?)<br />&nbsp;(.+?)</dt>',r.text)


#print issuetime,'\n\n',time,'\n\n',weather

#for (x,y) in weather:
#    print x,y,'\n'

print '发布时间： %s\n今天是%s\n今天天气：%s,%s' %(issuetime[0],time[0],weather[0][0],weather[0][1])







