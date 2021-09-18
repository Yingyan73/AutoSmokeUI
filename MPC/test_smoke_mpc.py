#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_smoke_mpc.py
# @Author: Xuewen Lei
# @Date  : 2021/9/17
# @Desc  :

import uiautomator2 as u2


class TestHPCSmoke:
    def setup_class(self):
        self.mpc = u2.connect("857353b4")
        print(self.mpc)
        self.mpc.implicitly_wait(5)

    def test_removeNotifications(self):
        BtnPower = self.mpc(resourceId='com.ff.hvac:id/hvac_btn_power')
        print(BtnPower.info)
        print(BtnPower.info.get('checked'))


