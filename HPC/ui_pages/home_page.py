#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : home_page.py
# @Author: Xuewen Lei
# @Date  : 2021/9/23
# @Desc  :
import uiautomator2 as u2

from Logger.mylog import logger
from devices_info import DevicesInfo


class HomePage:
    def sliding_display_carousel_channel_list(self, d: u2.Device):
        d(resourceId="com.android.systemui:id/home").click_exists(5)
        d(text="HOME").click_exists(5)
        # Not every sliding is successful, add while loop to make sure slide successfully.
        slide_times = 1
        while not d(resourceId="com.ff.iai.paxlauncher:id/channel_logo").exists(5):
            d.swipe(98, 518, 400, 518, 0.05)
            logger.info(f"slide carousel channel list {slide_times} times")
            slide_times += 1
        from HPC.ui_pages.carousel_channel_list_page import CarouselChannelListPage
        return CarouselChannelListPage()

    def swipe_up_on_main_screen(self, d: u2.Device):
        # swipe up
        d.swipe(1044, 847, 1044, 150)
        logger.info("swipe up")

    def swipe_down_on_main_screen(self, d: u2.Device):
        # swipe down
        d.swipe(1044, 150, 1044, 847)
        logger.info("swipe down")


if __name__ == '__main__':
    hp = HomePage()
    d = u2.connect(DevicesInfo.HPC_SERIALNO)
    # hp.swipe_up_on_main_screen(d)
    # d.sleep(5)
    # hp.swipe_down_on_main_screen(d)
    hp.sliding_display_carousel_channel_list(d)
    # hp.swipe_down_on_carousel_channel_list(d)
    # hp.swipe_up_on_carousel_channel_list(d)
