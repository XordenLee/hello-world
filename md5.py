# -*- coding: utf-8 -*-

import hashlib
import getpass
import time

def encrypt(content): #加密
    m = hashlib.md5()
    m.update(bytes(content, encoding='utf8'))
    return m.hexdigest()

def crack(n, pwd): #解密
    for i in range(10**n):
        t = str(i).zfill(n)
        e = encrypt(t)
        if e == pwd:
            return t

content = getpass.getpass("请输入加密内容：") #6位数最多耗时5秒，7位数最多耗时50秒
l = len(content)
PWD = encrypt(content)
t1 = time.time()
cr = crack(l, PWD)
t2 = time.time()
t = t2 - t1
print('解密出内容：', cr)
print('用时%.2f秒！' % t)
