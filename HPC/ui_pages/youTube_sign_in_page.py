#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : youTube_sign_in_page.py
# @Author: Xuewen Lei
# @Date  : 2021/9/23
# @Desc  :
import uiautomator2 as u2

from devices_info import DevicesInfo


class YouTubeSignInPage:
    def sign_in_youTubeTV_account(self, d: u2.Device):
        d(resourceId="identifierId", className="android.widget.EditText").send_keys(DevicesInfo.YOUTUBE_TV_ACCOUNT)
        d(text="Next", className="android.widget.Button").click(5)
        if d(resourceId="profileIdentifier", text=DevicesInfo.YOUTUBE_TV_ACCOUNT).exists(timeout=5):
            d(className="android.widget.EditText").send_keys(DevicesInfo.YOUTUBE_TV_PASSWD)
            d(text="Next", className="android.widget.Button").click(5)
        from HPC.ui_pages.home_page import HomePage
        return HomePage()

if __name__ == '__main__':
    ytb = YouTubeSignInPage()
    d = u2.connect(DevicesInfo.HPC_SERIALNO)
    ytb.sign_in_youTubeTV_account(d)
