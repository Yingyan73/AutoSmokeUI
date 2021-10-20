#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : base.py
# @Author: Xuewen Lei
# @Date  : 2021/9/6
# @Desc  :
# base_page.py 基类，init，
# 封装一些最基本的方法，便于后续维护
import logging

from uiautomator2 import Device

logging.basicConfig(level=logging.INFO)


class BasePage:

    def __init__(self, d: Device = None):
        # 初始化driver
        self.d = d

    # def find(self, by, value):
    #     logging.info.json(by)
    #     logging.info.json(value)
    #
    #     # 查找元素
    #     return self.driver.xpath()

    # def swipe_find(self, text, num=5):
    #     # num : 默认查找次数
    #     # 进入滑动查找，改变隐式等待时长，提高查找速度
    #     self.driver.implicitly_wait(1)
    #
    #     # 滑动查找，通过外部传递的num次数，决定查找次数
    #     for i in range(0, num):
    #         try:
    #             element = self.driver.xpath(f"//*[@text='{text}']")
    #             self.driver.implicitly_wait(5)
    #             # 如果找到了这个元素，则返回
    #             return element
    #         except Exception:
    #             print("未找到，滑动")
    #             # 滑动一页，继续查找
    #             size = self.driver.get_window_size()
    #             # self.driver.get_window_rect()
    #             width = size['width']
    #             height = size['height']
    #             # 'width', 'height'
    #             start_x = width / 2
    #             start_y = height * 0.8
    #
    #             end_x = start_x
    #             end_y = height * 0.3
    #
    #             duration = 2000  # ms
    #             # 完成滑动操作
    #             self.driver.swipe(start_x, start_y, end_x, end_y, duration)
    #         if i == num - 1:
    #             # 如果达到 num-1次没有找到，则抛出这个异常
    #             self.driver.implicitly_wait(5)
    #             raise Exception(f"找了{i}次，未找到")
