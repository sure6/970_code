#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project : 970_code
# @File    : week7-cracking_password.py
# @Author  : lee sure
# @Description :
# @Date    : 2023/4/24 22:45
# @Software : PyCharm

import hashlib
import time

def PermGen(char_set, max_len):
    if max_len <=0: return
    for c in char_set:
        yield c
    for c in char_set:
        for next in PermGen(char_set, max_len-1):
            yield c + next

if __name__=="__main__":

    start = time.time()
    given_value='hardd'
    result= PermGen('abcdefghijklmnopqrstuvwxyz',len(given_value))
    testhash =  hashlib.sha1(given_value.encode()).hexdigest()
    print(testhash)
    for item in list(result):
        hash_value=hashlib.sha1(item.encode()).hexdigest()
        if hash_value == testhash:
            print("Found: ",item)
            end = time.time()
            print("time required",end - start)
            break




