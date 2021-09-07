#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : vehicle.py
# @Author: Xuewen Lei
# @Date  : 2021/9/6
# @Desc  :
from page.app import App
from page.base import BasePage


class VehiclePage(BasePage):
    def enter_settings_page(self):
        self.d(text="SETTINGS").click()
        from page.settings import SettingsPage
        return SettingsPage()


