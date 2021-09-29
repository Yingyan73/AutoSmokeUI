#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : carousel_channel_list_page.py
# @Author: Xuewen Lei
# @Date  : 2021/9/29
from HPC.ui_pages.home_page import HomePage
from Logger.mylog import logger
import uiautomator2 as u2

from devices_info import DevicesInfo


class CarouselChannelListPage:
    def swipe_up_on_carousel_channel_list(self, d: u2.Device):
        # swipe up
        d.swipe(266, 929, 266, 251)
        logger.debug("swipe up on carousel channel list")
        return CarouselChannelListPage()

    def swipe_down_on_carousel_channel_list(self, d: u2.Device):
        # swipe down
        d.swipe(266, 251, 266, 929)
        logger.debug("swipe down on carousel channel list")

    def select_a_channel_to_play(self, d: u2.Device, channel_name, hp: HomePage):
        swipe_times = 1
        if not d(resourceId="com.ff.iai.paxlauncher:id/channel_name").exists:
            hp.sliding_display_carousel_channel_list(d)
        while not d(resourceId="com.ff.iai.paxlauncher:id/channel_name", text=channel_name).exists:
            self.swipe_up_on_carousel_channel_list(d)
            logger.debug(f"swipe times :{swipe_times}")
            swipe_times += 1
        logger.info("found the channel I want!")
        d(resourceId="com.ff.iai.paxlauncher:id/channel_name", text=channel_name).click_exists(5)
        logger.info(f"playback {channel_name}")


if __name__ == '__main__':
    d = u2.connect(DevicesInfo.HPC_SERIALNO)
    cclp = CarouselChannelListPage()
    cclp.select_a_channel_to_play(d, "NBA TV")
