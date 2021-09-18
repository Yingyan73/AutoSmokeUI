#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : utils.py
# @Author: Xuewen Lei
# @Date  : 2021/9/8
# @Desc  :
from uiautomator2 import Device


def input_on_keyboard(input:str):
    for letter in input.rsplit():
        print(letter)


if __name__ == '__main__':
    input_on_keyboard("ffcn.2020")
