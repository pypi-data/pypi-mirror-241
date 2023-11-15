# coding:utf-8 
# @Author : lizhankang
# @Subject :
from unittest import TestCase
from src.lizhankangpkg import *


# @Time : 2023 - 11 - 13
class Test(TestCase):
    def test_read_exel(self):
        read_exel('/Users/sqb/Desktop/副本新.xlsx')
