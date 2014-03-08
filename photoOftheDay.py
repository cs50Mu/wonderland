#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import requests
import sys
import re
import time

time.sleep(8)
reload(sys)
sys.setdefaultencoding('utf-8')
r = requests.get('http://feeds.nationalgeographic.com/ng/photography/photo-of-the-day/')
url = re.findall('http://[^\" ]*/exposure/[^\"]*',r.text)
url = re.sub('360x270','1600x1200',url[0])
with open('/home/linuxfish/.config/awesome/dailyPic.jpg','w') as f:
    f.write(requests.get(url).content)
