#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 06/17/2013 

"""download English Cafe from EslPod
"""

__revision__ = '0.1'


import requests
import sys
import os.path as path

url = 'http://traffic.libsyn.com/eslpod/EC'
for i in xrange(415,0,-1):
    link = '%s%d.mp3' %(url,i)
    print link
    filename = link.split('/')[-1]
    print filename
    r = requests.get(link,stream=True)   # set stream=True to prevent from reading the content at once into
    total_length = int(r.headers.get('content-length'))  # the memory,very useful for large files.
    print 'downloading %s...'  %filename
    if path.exists(filename) and path.getsize(filename) == int(total_length):
        print 'Warning: %s exists.skip..' %filename
        continue
    with open(filename,'wb') as f:
        if total_length is None:
            print 'No content-length found'
            f.write(r.content)
        else:
            dl = 0
            for data in r.iter_content(chunk_size=1024):  # read 1024 bytes each time
                dl += len(data)
                f.write(data)
                done = int(50. * dl / total_length)
                sys.stdout.write("\r[%s%s]\t%s/%s" %('=' * done,' ' * (50-done),str(dl),str(total_length)))
                sys.stdout.flush()  # fresh stdout

        print '\n%s downloaded..' %filename
