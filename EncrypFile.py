import os
from multiprocessing.pool import Pool
import codecs

import pyaes
import codecs
import os, shutil
# import importlib.util
from binascii import b2a_hex, a2b_hex
import math


from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex


def align(str, isKey=False):
    # 如果接受的字符串是密码，需要确保其长度为16
    if isKey:
        if len(str) > 16:
            return str[0:16]
        else:
            return align(str)
    # 如果接受的字符串是明文或长度不足的密码，则确保其长度为16的整数倍
    else:
        zerocount = 16-len(str) % 16
        for i in range(0, zerocount):
            str = str + '\0'
        return str

##加密文件中的内容
def encryto_file(in_filename):
    # in_filename = '../1.txt'
    #确保密码为16位
    key='hello python'
    key = align(key, True)
    key = key.encode('utf-8')

    out_encry_filename_ciphertext = 'encryp_files/' + in_filename
    in_filename='VOA2/'+str(in_filename)

    print('open in_filename   '+in_filename)
    f = codecs.open(in_filename, 'r',encoding='utf-8')
    plaintext = f.read()
    f.close()
    # print(plaintext)
    # key must be bytes, so we convert it



    plaintext=align(plaintext)
    plaintext=plaintext.encode('utf-8')
    print(out_encry_filename_ciphertext)

    aes = pyaes.AESModeOfOperationCTR(key)


    ciphertext = b2a_hex(aes.encrypt(plaintext)).decode("ASCII")

    ef = open(out_encry_filename_ciphertext, 'w')
    ef.write(ciphertext)
    ef.close()
    print('success write into file'+in_filename)


