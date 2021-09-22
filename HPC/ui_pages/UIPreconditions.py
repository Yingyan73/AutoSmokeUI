#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : UIPreconditions.py
# @Author: Xuewen Lei
# @Date  : 2021/9/18
# @Desc  :
import logging
import os

import uiautomator2 as u2

from devices_info import DevicesInfo

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s   %(levelname)s   %(message)s')


def ethernet_connectivity(ip, d: u2.Device):
    response = str(d.shell("ping " + ip))
    print(response)
    return response


class UIPreconditions:
    def connect_vpn(self, d: u2.Device):
        '''
        Precondition step on CHINA, If we want to test PAX on PID/RSD or Spotify,Alexa and other media apps on CID.
        :param d: input a uiautomator2 Device instance
        :return:
        '''
        # # Step1: confirm mpc and hpc network connection is normal
        # logging.info("Step1: confirm mpc and hpc network connection is normal")
        # res = ethernet_connectivity(DevicesInfo.MPC_IP, d)
        # if '64 bytes from 127.26.0.2' not in res:
        #     raise Exception('mpc and hpc network connection exception')
        # logging.info("connect normal with mpc")
        # # Step2: install VPN APK
        # logging.info("Step2: install VPN APK")
        # f = os.popen("adb install " + DevicesInfo.VPN_APK_PATH)
        # try:
        #     for line in f.readlines():
        #         logging.info("Console: " + line)
        # finally:
        #     f.close()  # this method must be called
        # # Step3: connect vpn account
        # # back to HOME page
        # logging.info("back to HOME page to launch AnyConnect app")
        d.implicitly_wait(5)
        # d.press("home")
        # # d(resourceId="com.android.systemui:id/home").click()
        # # display APPS page
        # d(text="APPS").click()
        # # launch AnyConnect app
        # d(resourceId="com.ff.iai.paxlauncher:id/appInfoTextView", text="AnyConnect").click()
        # # judge if disclaimer is pop-up
        # if d(resourceId="android:id/alertTitle").exists:
        #     d(resourceId="android:id/button1").click()
        # # Uncheck "Block Untrusted Servers" option
        # self.uncheck_block_untrusted_servers_option(d)

        # select a vpn to connect
        logging.info("select a vpn to connect")
        if d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/generic_list_item_value_text",
             text="No connection").exists(timeout=5):
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/generic_list_item_value_text",
              text="No connection").click(timeout=5)
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/tv_check_list_item_text").click(timeout=5)
            # set vpn ip
            logging.info("set vpn ip")
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/preference_summary", text="Not Set").click(timeout=5)
            d.send_keys("160.72.204.234:444", clear=True)
            d(resourceId="android:id/button1").click(timeout=5)
            d.sleep(2)
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/buttonbar_view_btn_positive").click(timeout=5)
            d.sleep(2)
            d(resourceId="com.android.systemui:id/back").click(timeout=5)
            d.sleep(2)
            # turn on VPN
            logging.info("turn on VPN")
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/cb_vpntoggle", text="Off").click(timeout=5)
            # pop-up notification and click "OK"
            d.sleep(2)
            # TODO 不能老用sleep，看看有没有别的方法
            self.pop_up_confrim(d)
            d.sleep(2)
            # select group to login
            if not d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/tv_PromptEntry_Combo").exists(timeout=5):
                raise Exception("current page is not select group")
            logging.info("select group to login")
            self.select_group_to_login(d)
        else:
            logging.info("already set vpn")
            # turn on VPN
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/cb_vpntoggle").click(timeout=5)
            # pop-up notification and click "OK"
            self.pop_up_confrim(d)
            # select group to login
            logging.info("select group to login")
            self.select_group_to_login(d)

    def pop_up_confrim(self, d: u2.Device):
        if d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/banner_title_bar",
             text="Security Warning: Untrusted Certificate").exists(timeout=5):
            d(resourceId="android:id/button1", text='Continue').click(timeout=5)
        # pop-up notification and click "OK"
        if d(resourceId="android:id/alertTitle",
             text="AnyConnect").exists(timeout=5):
            d.xpath('//*[@resource-id="android:id/buttonPanel"]/android.widget.LinearLayout[1]').click(timeout=5)

    def select_group_to_login(self, d: u2.Device):
        if d(resourceId="com.android.inputmethod.latin:id/keyboard_view").exists(timeout=5):
            d(description="Unknown character").click_exists(5)
        if d(resourceId="android:id/text1", index=5, text="FF_Gardena_Remote_NS").exists(timeout=5):
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/et_password").send_keys(DevicesInfo.PASSWD)
            d(resourceId="android:id/button1", text='Connect').click_exists(5)
            if d(resourceId="android:id/alertTitle", text='Connection request').exists(timeout=5):
                d(resourceId="android:id/button1", text='OK').click_exists(5)
        else:
            d.swipe(1044, 488, 1044, 359)
            d(resourceId="android:id/text1", index=5, text="FF_Gardena_Remote_NS").click_exists(5)
            d.sleep(2)
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/et_PromptEntry_Input").send_keys(DevicesInfo.ACCOUNT)
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/et_password").send_keys(DevicesInfo.PASSWD)
            d(resourceId="android:id/button1", text='Connect').click_exists(5)
            if d(resourceId="android:id/alertTitle", text='Connection request').exists(timeout=5):
                d(resourceId="android:id/button1", text='OK').click_exists(5)

    def uncheck_block_untrusted_servers_option(self, d: u2.Device):
        # make sure current page is anyconnect home page
        # TODO 是否需要改写为try except语法？
        d.sleep(5)
        if not d.xpath('//*[@resource-id="android:id/action_bar"]/android.widget.LinearLayout[2]').exists:
            raise Exception("current page is not anyconnect home page")
        d.xpath('//*[@resource-id="android:id/action_bar"]/android.widget.LinearLayout[2]').click()
        d(resourceId="android:id/title", text="Settings").click()
        # Uncheck "Block Untrusted Servers" option
        # TODO 要判断当前勾选状态再操作, checkbox选中后，属性没变化，无法判断。。。
        d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/preference_title",
          text="Block Untrusted Servers").click()
        d(resourceId="com.android.systemui:id/back").click()


if __name__ == '__main__':
    bsp = UIPreconditions()
    d = u2.connect(DevicesInfo.HPC_SERIALNO)
    # d.swipe(1044, 488, 1044, 359)
    bsp.connect_vpn(d)
