#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author:linuxfish.exe@gmail.com
# Last modified: 

"""docstring
"""

__revision__ = '0.1'

import logging; logging.basicConfig(level=logging.INFO)

import os,sys,os.path

sys.path.append(os.path.dirname(__file__))

from transwarp import db
from transwarp.web import WSGIApplication, Jinja2TemplateEngine

from config import configs

def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'一分钟前'
    elif delta < 3600:
        return u'%s分钟前' %( delta // 60)
    elif delta < 86400:
        return u'%s小时前' %( dalta // 3600)
    elif delta < 604800:
        return u'%s天前' %( delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year,dt.month,dt.day)

# init db
db.create_engine(**configs.db)

#init wsgi app
wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))

template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
template_engine.add_filter('datetime', datetime_filter)

wsgi.template_engine = template_engine

import urls

wsgi.add_module(urls)

if __name__ == '__main__':
    wsgi.run(9000)
