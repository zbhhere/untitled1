import os
from binascii import b2a_hex, a2b_hex
from multiprocessing.pool import Pool
import re
import pyaes
import locale
locale.getdefaultlocale()
i=0
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


#####解密
def decrypto_file(in_filename):
    global i
    key = 'hello python'
    key = align(key, True)
    key = key.encode('utf-8')
    # aes1 = pyaes.AESModeOfOperationCTR(key)

    # decrypted_out_filename=aes1.decrypt(a2b_hex(in_filename)).decode('utf-8')
    # decrypted_out_filename=decrypted_out_filename.replace('\0','')
    # print(len(decrypted_out_filename))
    # decrypted_out_filename=decrypted_out_filename.strip()
    # print(len(decrypted_out_filename))
    out_filename = os.path.join('DECRAPYFILES',in_filename)
    in_filename='encryp_files/'+in_filename

    # decrypted_out_filename=decrypted_out_filename.replace('.txt','')
    # print(decrypted_out_filename)
    print(out_filename)
    ff = open(in_filename, 'r',encoding='utf-8')
    ciphertext = ff.read()
    ff.close()

    aes2 = pyaes.AESModeOfOperationCTR(key)

    decrypted = aes2.decrypt(a2b_hex(ciphertext)).decode('utf-8')

    # fw = open('DECRAPYFILES/'+decrypted_out_filename, 'w',encoding='utf-8')
    fw = open(out_filename, 'w',encoding='utf-8')
    fw.write(decrypted)
    fw.close()

    # os.rename(out_filename,decrypted_out_filename)


    # print(decrypted)
if __name__=='__main__':
    pool=Pool(10)

    for parent,dirnames,filenames in os.walk('encryp_files/'):
        filename=[x for x in filenames]
        pool.map(decrypto_file,filename)
        pool.close()
        pool.join()

