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
    def playback_youTubeTV_by_swipe_up_and_down(self, d: u2.Device):
        # swipe up
        # d.swipe(1044, 847, 1044, 150)
        # swipe carousel channel list

        # d.swipe(130, 518, 300, 518, 0.5)
        # d.swipe_ext("right", box=(117, 509, 155, 509))
        # d.drag(117, 509, 155, 509)
        d.touch.move(117, 509).move(155, 509)
        logger.info("wipe carousel channel list")


if __name__ == '__main__':
    hp = HomePage()
    d = u2.connect(DevicesInfo.HPC_SERIALNO)
    hp.playback_youTubeTV_by_swipe_up_and_down(d)
