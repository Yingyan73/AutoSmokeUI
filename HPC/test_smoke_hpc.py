#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_smoke_hpc.py
# @Author: Xuewen Lei
# @Date  : 2021/9/15
# @Desc  :
import os

import uiautomator2 as u2

from HPC.bsp_steps.bsp_testcases import BSPTestCases, ethernet_connectivity
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

    # TODO 这三条可以用参数化改成一条case
    def test_ethernet_connectivity_mmu(self):
        # ping MMU
        res = ethernet_connectivity(DevicesInfo.MMU_IP, self.hpc)
        assert '64 bytes from 127.26.0.1' in res

    def test_ethernet_connectivity_iab(self):
        # ping IAB
        res = ethernet_connectivity(DevicesInfo.IAB_IP, self.hpc)
        assert '64 bytes from 127.26.0.4' in res

    def test_ethernet_connectivity_mpc(self):
        # ping MPC
        res = ethernet_connectivity(DevicesInfo.MPC_IP, self.hpc)
        assert '64 bytes from 127.26.0.2' in res

    def test_playBack_youTubeTV_on_home(self):
        pass
