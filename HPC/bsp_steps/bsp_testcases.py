#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : bsp_testcases.py
# @Author: Xuewen Lei
# @Date  : 2021/9/18
# @Desc  :
import os

import uiautomator2 as u2

from devices_info import DevicesInfo


def ethernet_connectivity(ip, d: u2.Device):
    response = str(d.shell("ping " + ip))
    print(response)
    return response


class BSPTestCases:

    def connect_vpn(self, d: u2.Device):
        # Step1: confirm mpc and hpc network connection is normal
        print("Step1: confirm mpc and hpc network connection is normal")
        res = ethernet_connectivity(DevicesInfo.MPC_IP, d)
        if '64 bytes from 127.26.0.2' not in res:
            raise Exception('mpc and hpc network connection exception')
        print("connect normal with mpc")
        # Step2: install VPN APK
        print("Step2: install VPN APK")
        f = os.popen("adb install " + DevicesInfo.VPN_APK_PATH)
        try:
            for line in f.readlines():
                if "Success" in line:
                    print("install vpn success!")
                print("Console: " + line)
        finally:
            f.close()  # this method must be called
        # Step3: connect vpn account
        # back to HOME page
        print("back to HOME page to launch AnyConnect app")
        d(resourceId="com.android.systemui:id/home").click()
        # display APPS page
        d(text="APPS").click()
        # launch AnyConnect app
        d(resourceId="com.ff.iai.paxlauncher:id/appInfoTextView", text="AnyConnect").click()
        # judge if disclaimer is pop-up
        if d(resourceId="android:id/alertTitle").exists:
            d(resourceId="android:id/button1").click()

        # Uncheck "Block Untrusted Servers" option
        self.uncheck_block_untrusted_servers_option(d)

        # select a vpn to connect
        print("select a vpn to connect")
        if d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/generic_list_item_value_text").get_text() == "No connection":  # TODO 还需要加已经设置过vpn的判断
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/generic_list_item_label_text",
              text="Connection").click()
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/tv_check_list_item_text").click()
            # set vpn ip
            print("set vpn ip")
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/preference_summary", text="Not Set").click()
            d.send_keys("160.72.204.234:444", clear=True)
            d(resourceId="android:id/button1").click()
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/buttonbar_view_btn_positive").click()
            d(resourceId="com.android.systemui:id/back").click()
            # turn on VPN
            print("turn on VPN")
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/cb_vpntoggle").click()
            # # Uncheck "Block Untrusted Servers" option
            # d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/preference_title",
            #   text="Block Untrusted Servers").click()
            # d(resourceId="com.android.systemui:id/back").click()
            # # turn on VPN after setting
            # d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/cb_vpntoggle").click()
            # d(resourceId="android:id/button1").click()
            # pop-up notification and click "OK"
            d.xpath('//*[@resource-id="android:id/buttonPanel"]/android.widget.LinearLayout[1]').click()
            # select group to login
            print("select group to login")
            self.select_group_to_login(d)

        else:
            print("already set vpn")
            # turn on VPN
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/cb_vpntoggle").click()
            # pop-up notification and click "OK"
            d.xpath('//*[@resource-id="android:id/buttonPanel"]/android.widget.LinearLayout[1]').click()
            # select group to login
            print("select group to login")
            self.select_group_to_login(d)

    def select_group_to_login(self, d):
        d(resourceId="android:id/text1").click()
        d(resourceId="android:id/text1", text="FF_Gardena_Remote_NS").click()
        d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/et_PromptEntry_Input").send_keys(DevicesInfo.ACCOUNT,
                                                                                               clear=True)
        d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/et_password").send_keys(DevicesInfo.PASSWD,
                                                                                      clear=True)
        d(resourceId="android:id/button1").click()

    def uncheck_block_untrusted_servers_option(self, d: u2.Device):
        # make sure current page is anyconnect home page
        # TODO 是否需要改写为try except语法？
        d.sleep(5)
        if not d.xpath('//*[@resource-id="android:id/action_bar"]/android.widget.LinearLayout[2]').exists:
            raise Exception("current page is not anyconnect home page")
        d.xpath('//*[@resource-id="android:id/action_bar"]/android.widget.LinearLayout[2]').click()
        d(resourceId="android:id/title", text="Settings").click()
        # Uncheck "Block Untrusted Servers" option
        # TODO 要判断当前勾选状态再操作
        d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/preference_title",
          text="Block Untrusted Servers").click()
        d(resourceId="com.android.systemui:id/back").click()


if __name__ == '__main__':
    bsp = BSPTestCases()
    d = u2.connect(DevicesInfo.HPC_SERIALNO)
    d.implicitly_wait(5)
    bsp.connect_vpn(d)
