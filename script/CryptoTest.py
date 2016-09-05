#coding=utf-8

from Crypto.Hash import MD5
from Crypto.Cipher import DES3

def _3des_encrypt():
    
    pass


def _3des_decrypt():
    pass


def md5(Msg):
    decrypter = MD5.new()
    decrypter.update(Msg)
    return decrypter.hexdigest()
    pass


if __name__ == '__main__':
    print(md5("123456"))
    pass