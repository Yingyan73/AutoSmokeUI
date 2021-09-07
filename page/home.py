#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : home.py
# @Author: Xuewen Lei
# @Date  : 2021/9/6
# @Desc  :
import logging

from page.base import BasePage

logging.basicConfig(level=logging.INFO)


class HomePage(BasePage):
    def enter_vehicle_page(self):
        self.d.xpath('//*[@resource-id="com.android.systemui:id/ff_car_navigation_bar_button_vehicle"]/android'
                          '.widget.LinearLayout[1]/android.widget.ImageButton[1]').click()
        from page.vehicle import VehiclePage
        return VehiclePage()

    def connect_bluetooth(self):
        pass

    def open_360camera(self):
        pass
