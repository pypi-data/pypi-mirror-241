# coding:utf-8 
# @Author : lizhankang
# @Subject : 
# @Time : 2023 - 11 - 09
import random
import string
import uuid
from .rsa import *
import pandas as pd

def welcome():
    for i in range(10):
        print("welcome to lizhankangpkg 滴滴滴 ...")


def gene_curl(curl_template, params):
    """
    使用python生成curl脚本
    tips: 非占位符的 {} 要使用 '{' '}'进行转译。如下模版
    :param curl_template: curl模版
    :param params: 变量，支持 list and dict
    :return: str
    """
    exa_curl_template = r'''
    curl --location 'http://er-receipt-core/rpc/receipt-layout' \
    --header 'Content-Type: application/json' \
    --data '{{
        "method": "storeBinding",
        "params": [
            {{
                "brand_code": {},
                "ka_store_sn": "{}",
                "receipt_layout_sn":"{}"
            }}
        ],
        "jsonrpc": "{}",
        "id": {}
    }}'
    '''

    exa_curl_template2 = r'''
    curl --location 'http://er-receipt-core/rpc/receipt-layout' \
    --header 'Content-Type: application/json' \
    --data '{{
        "method": "storeBinding",
        "params": [
            {{
                "brand_code": {brand_code},
                "ka_store_sn": "{ka_store_sn}",
                "receipt_layout_sn":"{receipt_layout_sn}"
            }}
        ],
        "jsonrpc": "{jsonrpc}",
        "id": {id}
    }}'
    '''

    formatted_result = ''
    # 使用字符串的 format 方法一次性替换多个值
    if isinstance(params, list):
        formatted_result = curl_template.format(*params)
    if isinstance(params, dict):
        formatted_result = curl_template.format(**params)
    # 打印生成的字符串
    print(formatted_result)



def read_txt_file(your_file, size=1000):
    """
    读取文件内容打印并返回
    :param your_file:
    :param size:
    :return: 文件内容
    """
    with open(your_file, mode='r', encoding='utf-8') as file:
        batch_size = size
        file_content = []
        while True:
            batch = [next(file) for _ in range(batch_size)]
            if not batch:
                break
            # if len(batch) < batch_size:
            #     # 处理不足1000行的最后一个批次
            #     # 在这里处理不足1000行的情况
            #     for line in batch:
            #         print(line.strip())  # 以示例，这里只是打印每行数据
            # else:
            #     # 处理完整的1000行数据
            #     for line in batch:
            #         print(line.strip())  # 以示例，这里只是打印每行数据
            for line in batch:
                print(line.strip())
                file_content.append(line)
        return file_content


def read_excel(excel_path, sheet_name="Sheet1"):
    """
    读取excel文件转成字典格式
    :param excel_path:
    :param sheet_name:
    :return:
    """
    global df
    try:
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
    except Exception as exception:
        print(exception)
    # df = pd.read_excel(excel_path, sheet_name=sheet_name)
    # 将DataFrame转换为字典
    product_list = df.to_dict(orient='records')  # orient='records'参数表示将每一行转换为一个字典
    print(product_list)



def unique_random(len_unique_num):
    """
    生成一个长度为 leng_unique 的随机数(不保证绝绝对对唯一，但是基本上不会出现重复的情况)
    :param len_unique_num: 期望随机数的长度
    :return:
    :return type: str
    """
    num = uuid.uuid4().int
    len_num = len(str(num))
    start_index = random.choice(range(len_num - len_unique_num + 1))
    end_index = start_index + len_unique_num
    return str(num)[start_index:end_index]

def gen_random_str(length):
    """
    生成指定长度的字符串
    :param length:
    :return:
    """
    # 可以定义字符集，根据需要自定义
    characters = string.ascii_letters + string.digits  # 包括字母和数字
    # 如果你需要包括特殊字符，可以添加如下：
    # characters = string.ascii_letters + string.digits + string.punctuation

    # 使用随机函数生成指定长度的随机字符串
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string