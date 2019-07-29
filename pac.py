# ！/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'zhangjing'
import requests

response = requests.get(url='http://www.autohome.com.cn/news/')
print("22")
print(response.text)