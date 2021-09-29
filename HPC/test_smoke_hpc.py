#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_smoke_hpc.py
# @Author: Xuewen Lei
# @Date  : 2021/9/15
# @Desc  :

import pytest
import uiautomator2 as u2

import status
from HPC.BSP.bsp_steps import ethernet_connectivity
from HPC.ui_pages.home_page import HomePage
from HPC.ui_pages.youTube_sign_in_page import YouTubeSignInPage
from devices_info import DevicesInfo

'''
1. Setup
  download daily version and fastboot flash software

Testcases:
    BSP testcases
        1. HPC reboot: HPC, MPC, Adaptor and MMU working together, and then reboot HPC, after reboot, check if Ethernet/Touch/display/WiFi/BT work
        2. Interior Camera: Check Interior Camera
        3. MCU: Check MCU control Fan driver power and PWM for fan speed.
    UI testcases
        1. PID SocialApps: Check video call and text messaging for Hangouts, Zoom or Wechat
        2. VideoStreaming: Check VideoStreaming including Youtube, Amazon video and Netflix via app or browser
'''


class TestHPCSmoke:

    def setup_class(self):
        self.hpc = u2.connect(DevicesInfo.HPC_SERIALNO)
        print(self.hpc.info)
        self.hpc.implicitly_wait(5)
        self.home_page = HomePage()
        # TODO 感觉还是用fixtures好一些
        # if DevicesInfo.TEST_ENVIRONMENT is "CH" and status.if_vpn_connected is False:
        #     from HPC.ui_pages.ui_preconditions import UIPreconditions
        #     setup = UIPreconditions()
        #     setup.connect_vpn(self.hpc)

    @pytest.mark.parametrize('ip,result', [[DevicesInfo.MMU_IP, '64 bytes from 127.26.0.1'],
                                           [DevicesInfo.IAB_IP, '64 bytes from 127.26.0.4'],
                                           [DevicesInfo.MPC_IP, '64 bytes from 127.26.0.2']], ids=['MMU', 'IAB', 'MPC'])
    def test_ethernet_connectivity(self, ip, result):
        # ping MMU,IAB,MPC
        res = ethernet_connectivity(ip, self.hpc)
        assert result in res

    def test_playBack_youTubeTV_on_home(self, connect_vpn):
        if DevicesInfo.TEST_ENVIRONMENT is 'CH' and status.if_vpn_connected is False:
            connect_vpn()
        if not status.if_youTube_sign_in:
            YouTubeSignInPage() \
                .sign_in_youTubeTV_account(self.hpc) \
                .sliding_display_carousel_channel_list(self.hpc) \
                .swipe_up_on_carousel_channel_list(self.hpc) \
                .select_a_channel_to_play(self.hpc, 'ESPN', self.home_page)
        else:
            self.home_page.sliding_display_carousel_channel_list(self.hpc) \
                .swipe_up_on_carousel_channel_list(self.hpc) \
                .select_a_channel_to_play(self.hpc, 'ESPN', self.home_page)

    def test_playBack_amazon_video_on_foryou(self):
        pass

    def test_play_youTube_video_on_videos(self):
        pass
