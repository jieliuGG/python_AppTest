# —— coding :utf-8 ——
# @time:    2020/10/1 12:08
# @IDE:     py_AppTest_Frameworkv1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    conftest.py
from Common.dir_config import *
import yaml
from appium import webdriver
import pytest

from PageOjects.Common_Bus import CommonBus


@pytest.fixture
def startApp():
    # 准备服务器参数，与appium server进行连接。noReset=True
    driver = baseDriver()
    # 1. 判断欢迎页面是否存在
    CommonBus(driver).handle_welcome_page()
    # 2. 判断当前用户是否已登录，没有登录则进行登录状态
    # 3. 是否有手势设置密码框，不设置
    CommonBus(driver).is_setGesture()

def baseDriver(server_port=4723, noReset=None, automationName=None, **kwargs):
    # 将默认配置参数读取出来
    fs = open(Desired_Caps_dir + '/desired_caps.yaml')
    desired_caps = yaml.load(fs)
    # 参数调用
    if noReset is not None:
        desired_caps['noReset'] = noReset
    if automationName is not None:
        desired_caps['automationName'] = automationName
    # 返回一个启动对象--driver
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(server_port), desired_caps)
