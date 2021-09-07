#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : settings.py
# @Author: Xuewen Lei
# @Date  : 2021/9/6
# @Desc  :
from page.base import BasePage


class SettingsPage(BasePage):

    def enter_connectivity_page(self):
        self.d(resourceId="com.ff.vehicle:id/tv_list_title", text="Connectivity").click()
        from page.connectivity import ConnectivityPage
        return ConnectivityPage()
