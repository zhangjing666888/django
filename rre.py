# ！/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'zhangjing'

import redis
r=redis.Redis(host='127.0.0.1',port=6379)
r.set('foo','Bar')


print(r.get('foo'))