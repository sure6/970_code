#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project : 970_code 
# @File    : week9-10-regex.py
# @Author  : lee sure
# @Description : practice regular expression
# @Date    : 2023/5/10 19:50 
# @Software : PyCharm

import re
# log_file = input ("Enter file name: ")

f=open("access.log", "r")
pattern_ip_address = r"\d+\.\d+\.\d+\.\d+"
pattern_website = r"http(s?)://(\S+)"
while True:
    line = f.readline()
    if not line:
        break
    if re.search(pattern_ip_address, line):
        print(line.strip())
f.close()