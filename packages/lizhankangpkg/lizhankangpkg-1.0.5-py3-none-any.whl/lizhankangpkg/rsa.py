# coding:utf-8 
# @Author : lizhankang
# @Subject : 
# @Time : 2023 - 11 - 09
import json
import base64
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def signer(data_dict, key_path =""):
    """
    加签
    :param data_dict: 待签名dict对象
    :param key_path: 密钥路径
    :return: 签名(str)
    """
    if key_path == "":
        print("请输入密钥路径")
        return
    with open(key_path, mode='rb') as f:
        rsa_private_key = RSA.import_key(f.read())
    secret_key_obj = PKCS1_v1_5.new(rsa_private_key)
    request_hash = SHA256.new(json.dumps(data_dict, separators=(',', ':'), ensure_ascii=False).encode('utf-8'))
    return base64.b64encode(secret_key_obj.sign(request_hash)).decode('utf-8')
