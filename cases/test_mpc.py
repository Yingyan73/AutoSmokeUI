#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_mpc.py
# @Author: Xuewen Lei
# @Date  : 2021/9/6
# @Desc  :

from page.app import App

class TestMPC:

    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.home = self.app.goto_main()

    def teardowm(self):
        self.app.restart()

    def test_connect_wifi(self):
        self.home.enter_vehicle_page() \
            .enter_settings_page().enter_connectivity_page().connect_wifi()
        print(self.home.d(resourceId="com.ff.vehicle:id/wifi_state_tv").get_text())

    def test_setup(self):
        self.home.d.app_start("com.android.systemui","com.android.car.overview.StreamOverviewActivity")
