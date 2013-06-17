#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 06/17/2013 

"""download cs75 video courses
"""

__revision__ = '0.1'


import requests
import re
import time
import sys
import os.path as path

url = 'http://cs75.tv/2010/fall/'
print 'fetching video links..'
r = requests.get(url)
links = re.findall("http://cdn.cs75.net/2010/fall/lectures/[^<>]+?\.mp4",r.text)
links = sorted(list(set(links)))
print 'done!'
print links
for link in links:
    filename = link.split('/')[-1]
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
