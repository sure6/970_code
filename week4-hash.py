#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project : 970_code 
# @File    : week4-hash.py
# @Author  : lee sure
# @Description : 
# @Date    : 2023/4/24 22:45 
# @Software : PyCharm

import hashlib

text= input("please enter you text: ")
hashvalue_md5 = hashlib.md5(text.encode())
print("{0} has size of {1}  bytes: {2}".format(hashvalue_md5.name,hashvalue_md5.digest_size,hashvalue_md5.hexdigest()))
hashvalue_sha1 = hashlib.sha1(text.encode())
print("{0} has size of {1}  bytes: {2}".format(hashvalue_sha1.name,hashvalue_sha1.digest_size,hashvalue_sha1.hexdigest()))
hashvalue_sha256 = hashlib.sha256(text.encode())
print("{0} has size of {1}  bytes: {2}".format(hashvalue_sha256.name,hashvalue_sha256.digest_size,hashvalue_sha256.hexdigest()))
hashvalue_sha384 = hashlib.sha384(text.encode())
print("{0} has size of {1}  bytes: {2}".format(hashvalue_sha384.name,hashvalue_sha384.digest_size,hashvalue_sha384.hexdigest()))
hashvalue_sha512 = hashlib.sha512(text.encode())
print("{0} has size of {1}  bytes: {2}".format(hashvalue_sha512.name,hashvalue_sha512.digest_size,hashvalue_sha512.hexdigest()))