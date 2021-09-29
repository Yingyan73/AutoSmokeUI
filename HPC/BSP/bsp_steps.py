#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : bsp_steps.py
# @Author: Xuewen Lei
# @Date  : 2021/9/23


import uiautomator2 as u2

from Logger.mylog import logger
from devices_info import DevicesInfo


def ethernet_connectivity(ip, d: u2.Device):
    response = str(d.shell("ping " + ip))
    print(response)
    return response


def checking_internet_access(d: u2.Device, domain_name: str):
    logger.info(f"Step1: confirm hpc can access {domain_name}")
    if "baidu" in domain_name.lower():
        res = ethernet_connectivity(DevicesInfo.BAIDU_DOMAIN_NAME, d)
        if '64 bytes from' not in res:
            logger.error(f'hpc can not access {domain_name}')
        logger.info("access network success")
    elif "google" in domain_name.lower():
        res = ethernet_connectivity(DevicesInfo.GOOGLE_DOMAIN_NAME, d)
        if '64 bytes from' not in res:
            logger.error(f'hpc can not access {domain_name}')
        logger.info("access network success")

