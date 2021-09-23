#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : UIPreconditions.py
# @Author: Xuewen Lei
# @Date  : 2021/9/18
# @Desc  :

import os

import uiautomator2 as u2

from HPC.BSP.bsp_steps import checking_internet_access
from Logger.mylog import logger
from devices_info import DevicesInfo


class UIPreconditions:
    def connect_vpn(self, d: u2.Device):
        '''
        Precondition step on CHINA, If we want to test PAX on PID/RSD or Spotify,Alexa and other media apps on CID.
        :param d: input a uiautomator2 Device instance
        :return:
        '''
        # Step1: confirm mpc and hpc network connection is normal
        checking_internet_access(d, "baidu")
        # TODO ping baidu，确认外网连接正常
        # Step2: install VPN APK
        logger.info("Step2: install VPN APK")
        f = os.popen("adb install " + DevicesInfo.VPN_APK_PATH)
        try:
            for line in f.readlines():
                logger.info("Console: " + line)
        finally:
            f.close()  # this method must be called
        # Step3: connect vpn account
        # back to HOME page
        logger.info("back to HOME page to launch AnyConnect app")
        d.implicitly_wait(5)
        # d(resourceId="com.android.systemui:id/home").click()
        # display APPS page
        if not d(text="APPS").exists(timeout=3):
            d.press("home")
            d(text="APPS").click_exists(5)
        # launch AnyConnect app
        if not d(resourceId="com.ff.iai.paxlauncher:id/appInfoTextView", text="AnyConnect").exists(timeout=3):
            for i in range(0, 6):
                d(text="APPS").click()
            d(resourceId="com.ff.iai.paxlauncher:id/appInfoTextView", text="AnyConnect").click_exists(5)
        else:
            d(resourceId="com.ff.iai.paxlauncher:id/appInfoTextView", text="AnyConnect").click_exists(5)
        # judge if disclaimer is pop-up
        if d(resourceId="android:id/alertTitle", text="AnyConnect").exists(timeout=3):
            d(resourceId="android:id/button1", text="OK").click_exists(5)
        # Uncheck "Block Untrusted Servers" option
        if not self.uncheck_block_untrusted_servers_option(d):
            return False

        # select a vpn to connect
        logger.info("select a vpn to connect")
        if d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/generic_list_item_value_text",
             text="No connection").exists(timeout=5):
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/generic_list_item_value_text",
              text="No connection").click(timeout=5)
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/tv_check_list_item_text").click(timeout=5)
            # set vpn ip
            logger.info("set vpn ip")
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/preference_summary", text="Not Set").click(timeout=5)
            d.send_keys("160.72.204.234:444", clear=True)
            d(resourceId="android:id/button1").click(timeout=5)
            d.sleep(2)
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/buttonbar_view_btn_positive").click(timeout=5)
            d.sleep(2)
            d(resourceId="com.android.systemui:id/back").click(timeout=5)
            d.sleep(2)
            # turn on VPN
            logger.info("turn on VPN")
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/cb_vpntoggle", text="Off").click(timeout=5)
            # pop-up notification and click "OK"
            d.sleep(2)
            # TODO 不能老用sleep，看看有没有别的方法
            self.pop_up_confrim(d)
            # select group to login
            if not d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/tv_PromptEntry_Combo").exists(timeout=20):
                logger.error("current page is not select group")
                return False
            logger.info("select group to login")
            self.select_group_to_login(d)
            if d(className="android.widget.Switch", text='On').exists(timeout=10) and \
                    d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/generic_list_item_value_text",
                      text="Connected").exists(timeout=10):
                return True
        else:
            logger.info("already set vpn")
            # turn on VPN
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/cb_vpntoggle").click(timeout=5)
            # pop-up notification and click "OK"
            self.pop_up_confrim(d)
            # select group to login
            logger.info("select group to login")
            d.sleep(2)
            self.select_group_to_login(d)
            if d(className="android.widget.Switch", text='On').exists(timeout=10) and \
                    d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/generic_list_item_value_text",
                      text="Connected").exists(timeout=10):
                return True

    def pop_up_confrim(self, d: u2.Device):
        if d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/banner_title_bar",
             text="Security Warning: Untrusted Certificate").exists(timeout=5):
            d(resourceId="android:id/button1", text='Continue').click(timeout=5)
        # pop-up notification and click "OK"
        if d(resourceId="android:id/alertTitle",
             text="AnyConnect").exists(timeout=5):
            d.xpath('//*[@resource-id="android:id/buttonPanel"]/android.widget.LinearLayout[1]').click(timeout=5)

    def select_group_to_login(self, d: u2.Device):
        # TODO 再优化一下，写得太啰嗦了
        self.hide_keyboard(d)

        if d(resourceId="android:id/text1", text='Cert_Based').exists(timeout=5):
            d(className="android.widget.Spinner").click_exists(5)
            d.sleep(2)
            d.swipe(1044, 488, 1044, 359)
            d(resourceId="android:id/text1", index=5, text="FF_Gardena_Remote_NS").click_exists(5)
            d.sleep(2)
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/et_PromptEntry_Input").send_keys(DevicesInfo.ACCOUNT)
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/et_password").send_keys(DevicesInfo.PASSWD)
            d(resourceId="android:id/button1", text='Connect').click_exists(5)
            if d(resourceId="android:id/alertTitle", text='Connection request').exists(timeout=5):
                d(resourceId="android:id/button1", text='OK').click_exists(5)
        self.hide_keyboard(d)
        if d(resourceId="android:id/text1", index=5, text="FF_Gardena_Remote_NS").exists(timeout=5):
            d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/et_password").send_keys(DevicesInfo.PASSWD)
            d(resourceId="android:id/button1", text='Connect').click_exists(5)
            if d(resourceId="android:id/alertTitle", text='Connection request').exists(timeout=5):
                d(resourceId="android:id/button1", text='OK').click_exists(5)

    def hide_keyboard(self, d: u2.Device):
        if d(resourceId="com.android.inputmethod.latin:id/keyboard_view").exists(timeout=5):
            d(description="Unknown character").click_exists(5)
            logger.info("hide keyboard success!")

    def uncheck_block_untrusted_servers_option(self, d: u2.Device):
        # make sure current page is anyconnect home page
        # TODO 是否需要改写为try except语法？
        d.sleep(5)
        if not d.xpath('//*[@resource-id="android:id/action_bar"]/android.widget.LinearLayout[2]').exists:
            logger.error("current page is not anyconnect home page")
            return False
        d.xpath('//*[@resource-id="android:id/action_bar"]/android.widget.LinearLayout[2]').click()
        d(resourceId="android:id/title", text="Settings").click()
        # Uncheck "Block Untrusted Servers" option
        # TODO 要判断当前勾选状态再操作, checkbox选中后，属性没变化，无法判断。。。
        d(resourceId="com.cisco.anyconnect.vpn.android.avf:id/preference_title",
          text="Block Untrusted Servers").click()
        d(resourceId="com.android.systemui:id/back").click()
        return True


if __name__ == '__main__':
    bsp = UIPreconditions()
    d = u2.connect(DevicesInfo.HPC_SERIALNO)
    # d.swipe(1044, 488, 1044, 359)
    bsp.connect_vpn(d)
