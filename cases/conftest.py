#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : conftest.py
# @Author: Xuewen Lei
# @Date  : 2021/9/8
# @Desc  :
import pytest
import uiautomator2 as u2


@pytest.fixture
def disconnect_wifi():
    # disconnect wifi
    print("disconnect wifi")

