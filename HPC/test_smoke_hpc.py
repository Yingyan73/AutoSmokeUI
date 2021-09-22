#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_smoke_hpc.py
# @Author: Xuewen Lei
# @Date  : 2021/9/15
# @Desc  :

import pytest
import uiautomator2 as u2

from HPC.ui_pages.UIPreconditions import BSPTestCases, ethernet_connectivity
from devices_info import DevicesInfo

'''
1. Setup
  download daily version and fastboot flash software

Testcases:
    bsp_steps testcases
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
        print(self.hpc)
        self.hpc.implicitly_wait(5)
        self.bsp = BSPTestCases()

    @pytest.mark.parametrize('ip,result', [[DevicesInfo.MMU_IP, '64 bytes from 127.26.0.1'],
                                           [DevicesInfo.IAB_IP, '64 bytes from 127.26.0.4'],
                                           [DevicesInfo.MPC_IP, '64 bytes from 127.26.0.2']], ids=['MMU', 'IAB', 'MPC'])
    def test_ethernet_connectivity(self, ip, result):
        # ping MMU,IAB,MPC
        res = ethernet_connectivity(ip, self.hpc)
        assert result in res

    def test_playBack_youTubeTV_on_home(self):
        pass