import hashlib
import random

def get_Salt():
    l = '1234567890qwertyhujiklsdfgbhnm,./[\lzxcvnm'
    salt = ''.join(random.sample(l, 6))
    return salt

def hash_code():
    # 通过模块构造出一个hash对象
    h = hashlib.md5()
    # 通过hash对象的方法添加我要加密字符串
    pwd = '123456'
    pwd += get_Salt()
    h.update(pwd.encode())
    # 获得字符串类型的加密后的密文
    h.hexdigest()
    print(h.hexdigest())

hash_code()



