#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project : 970_code
# @File    : week3-symenc.py
# @Author  : lee sure
# @Description :
# @Date    : 2023/4/24 22:45
# @Software : PyCharm

from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key() 
    return key

def encrypt(key, ptext):
    ctext=Fernet(key).encrypt(ptext)
    return ctext

def decrypt(key, ctext): 
    ptext = Fernet(key).decrypt(ctext)
    return ptext

secretkey = create_key() 
print("Encryption Key:", secretkey)
plaintext=input("Enter your message to encrypt: ")
ciphertext= encrypt(secretkey, plaintext.encode())
print("Ciphertext: ", ciphertext)
plaintext_decrypt = decrypt(secretkey, ciphertext)
print("type:", type(plaintext_decrypt))
print("Plaintext (decrypted): ", decrypt(secretkey, ciphertext))
print("Plaintext (decrypted): "+ decrypt(secretkey, ciphertext).decode())