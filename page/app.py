#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : app.py
# @Author: Xuewen Lei
# @Date  : 2021/9/6
# @Desc  :
import logging

import uiautomator2 as u2

from page.home import HomePage

logging.basicConfig(level=logging.INFO)


class App:

    def __init__(self):
        self.d = u2.connect("857353b4")

    def start(self):
        if self.d is None:
            self.d = u2.connect("857353b4")
            logging.info(self.d.info)
            self.d.implicitly_wait(5)
        else:
            # reuse driver
            logging.info("reuse driver")
            self.d.app_start("com.android.systemui","com.android.car.overview.StreamOverviewActivity")
        return self

    def restart(self):
        # close_app() 关闭应用
        logging.info("restart app")
        self.d.app_clear("com.android.systemui")
        self.d.app_start("com.android.systemui","com.android.car.overview.StreamOverviewActivity")

    def stop(self):
        # quit() 销毁这个driver
        logging.info("quit app")
        self.d.app_stop("com.android.systemui")

    def clear(self):
        logging.info("Stop and clear app data")
        self.d.app_clear("com.android.systemui")

    def goto_main(self):
        # 入口
        logging.info("go to HomePage")
        return HomePage(self.d)
