#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project : 970_code
# @File    : week6-verifypwd.py
# @Author  : lee sure
# @Description :
# @Date    : 2023/4/24 22:45
# @Software : PyCharm

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
salt = b'\x99Q\xde\x13\x1e\xebzY\x9fq\xfa\x1dL\xf3\xc4\xb1'
key = b'\x01\xa9\x80M\xc8\xfa-`K\x00\xe8\xb2\x92v \n\xc8\xcc\xd2\xbdi{\xe6\r\xa0Z]\xde\x82\xebTG'
kdf = Scrypt(salt=salt, length =32, n=2**14, r=8, p=1,backend=default_backend())
password = input("What is your password?")
print(password.encode())

try:
    kdf.verify(password.encode(),key)
    print("yes, matched")
except:
    print("An exception occurred")