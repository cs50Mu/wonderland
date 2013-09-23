#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author: linuxfish.exe@gmail.com
# Last modified: 06/12/2013

"""
a commandline translator using youdao api
"""

__revision__ = '0.1'


import requests

para = {'keyfrom':'pusuerMu','key':'1788502748','type':'data','doctype':'json','version':'1.1'}

query = raw_input('主人，你想查神马？ ')
para['q'] = query

while True:
    if query == '.':
        break
    r = requests.get('http://fanyi.youdao.com/openapi.do',params = para)
    json = r.json()
    errorCode = json['errorCode']
    if errorCode != 0:
        print '出错啦！'
        break
    try:
        basic = json['basic']
        web = json['web']
        print '#############Basic#############\n'
        print u'解释：%s\n' %(basic['explains'][0])
        print u'音标：%s\n' %(basic['phonetic'])
        print '#############Web#############\n'
        for i in range(len(web)):
            print web[i]['key'],':'
            for j in range(len(web[i]['value'])):
                print web[i]['value'][j],
            print '\n'
        query = raw_input('主人，你想查神马？ ')
        para['q'] = query
    except:
        print '出错啦！'
        break



