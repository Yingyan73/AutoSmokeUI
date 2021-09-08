#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : connectivity.py
# @Author: Xuewen Lei
# @Date  : 2021/9/6
# @Desc  :
from page.base import BasePage


class ConnectivityPage(BasePage):
    def connect_wifi(self):

        self.d(resourceId="com.ff.vehicle:id/wifi_name_tv", text="FF-Web").click()
        self.d(resourceId="com.ff.vehicle:id/text_et").click()
        self.d(description="f").click()
        self.d(description="f").click()
        self.d(description="c").click()
        self.d(description="n").click()
        self.d(description=".").click()
        self.d(description="2").click()
        self.d(description="0").click()
        self.d(description="2").click()
        self.d(description="0").click()
        self.d(resourceId="com.ff.vehicle:id/ok_btn").click()
