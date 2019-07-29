# ！/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'zhangjing'

import random
def  maopao_sort(li):
    for i in range(len(li)-1):#运行多少趟
        for j in range(len(li)- i -1):#每趟交换几次
            if li[j] > [j+1]:
                li[j],li[j+1] = li[j+1],li[j]#前后互换

data =list(range(100)) #定义一个一到100的列表
random.shuffle(data)  #将列表打成无序的
print(data)
maopao_sort(data)
print(data)

