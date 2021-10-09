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
        swipe_up_times = 1
        swipe_down_times = 1
        found_last_channel = False
        found_first_channel = False
        if not d(resourceId="com.ff.iai.paxlauncher:id/channel_name").exists:
            hp.sliding_display_carousel_channel_list(d)
        while not d(resourceId="com.ff.iai.paxlauncher:id/channel_name", text=channel_name).exists:
            if found_last_channel is False and not d(resourceId="com.ff.iai.paxlauncher:id/channel_name",
                                                     text="truTV").exists:
                self.swipe_up_on_carousel_channel_list(d)
                logger.debug(f"swipe up times :{swipe_up_times}")
                swipe_up_times += 1
                if d(resourceId="com.ff.iai.paxlauncher:id/channel_name", text="truTV").exists:
                    found_last_channel = True
            elif found_first_channel is False and not d(resourceId="com.ff.iai.paxlauncher:id/channel_name",
                                                        text="ABC News Live").exists:
                logger.debug("swipe to first page and can't find the channel I want, try to swipe down to find it.")
                self.swipe_down_on_carousel_channel_list(d)
                logger.debug(f"swipe down times :{swipe_down_times}")
                swipe_down_times += 1
                if d(resourceId="com.ff.iai.paxlauncher:id/channel_name",
                     text="ABC News Live").exists:
                    found_first_channel = True
        logger.info("found the channel I want!")
        d(resourceId="com.ff.iai.paxlauncher:id/channel_name", text=channel_name).click_exists(5)
        logger.info(f"playback {channel_name}")


if __name__ == '__main__':
    d = u2.connect(DevicesInfo.HPC_SERIALNO)
    cclp = CarouselChannelListPage()
    hp = HomePage()
    while True:
        cclp.select_a_channel_to_play(d, "NBA TV", hp)
        d.sleep(600)
        cclp.select_a_channel_to_play(d, "MLB Network", hp)
        d.sleep(600)
