#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : home_page.py
# @Author: Xuewen Lei
# @Date  : 2021/9/23
# @Desc  :
import uiautomator2 as u2


class HomePage:
    def goto_youTube_signin_page(self, d: u2.Device):
        d(resourceId="com.android.systemui:id/home").click()
