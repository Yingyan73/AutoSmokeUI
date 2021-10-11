#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_smoke_hpc.py
# @Author: Xuewen Lei
# @Date  : 2021/9/15
# @Desc  :

import pytest
import uiautomator2 as u2

from HPC.BSP.bsp_steps import ethernet_connectivity, checking_internet_access
from HPC.ui_pages.home_page import HomePage
from HPC.ui_pages.ui_preconditions import UIPreconditions
from HPC.ui_pages.youTube_sign_in_page import YouTubeSignInPage
from Logger.mylog import logger
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
        self.youTube_signin = YouTubeSignInPage()
        self.uip = UIPreconditions()

    @pytest.mark.parametrize('ip,result', [[DevicesInfo.MMU_IP, '64 bytes from 127.26.0.1'],
                                           [DevicesInfo.IAB_IP, '64 bytes from 127.26.0.4'],
                                           [DevicesInfo.MPC_IP, '64 bytes from 127.26.0.2']], ids=['MMU', 'IAB', 'MPC'])
    def test_ethernet_connectivity(self, ip, result):
        # ping MMU,IAB,MPC
        res = ethernet_connectivity(ip, self.hpc)
        assert result in res

    @pytest.mark.dependency()
    def test_access_internet(self):
        if DevicesInfo.TEST_ENVIRONMENT is 'CH' and self.uip.if_vpn_connected is False:
            self.uip.connect_vpn(self.hpc)
        assert checking_internet_access(self.hpc, "google")

    # @pytest.mark.dependency(depends=["test_access_internet"])
    @pytest.mark.parametrize('channel_name', [["ESPN"]], ids=['ESPN'])
    def test_playBack_youTubeTV_on_home(self,channel_name):
        self.hpc(resourceId="com.android.systemui:id/home").click_exists(5)
        self.hpc.xpath('//android.widget.FrameLayout[1]').click_exists(5)
        if self.hpc(resourceId="headingText", text="Sign in").exists(10) and not self.youTube_signin.if_youTube_signin:
            logger.info("sign in youTube account")
            self.home_page = self.youTube_signin \
                .sign_in_youTubeTV_account(self.hpc)

        self.home_page.sliding_display_carousel_channel_list(self.hpc) \
            .select_a_channel_to_play(self.hpc, channel_name, self.home_page) \
            .confirm_selected_channel(self.hpc, channel_name, self.home_page)
        self.hpc.sleep(5)
        # TODO 断言需要再优化一下
        self.hpc.click(977, 776)
        if self.hpc(className="android.view.View", text=channel_name).exists(5):
            pass


    def test_playBack_amazon_video_on_foryou(self):
        pass

    def test_play_youTube_video_on_videos(self):
        pass
