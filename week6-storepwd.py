#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project : 970_code
# @File    : week6-storepwd.py
# @Author  : lee sure
# @Description :
# @Date    : 2023/4/24 22:45
# @Software : PyCharm

import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
salt = os.urandom(16)
kdf = Scrypt(salt=salt, length =32, n=2**14, r=8, p=1,backend=default_backend())
key = kdf.derive(b'csit970*')
print(salt)
print(key)