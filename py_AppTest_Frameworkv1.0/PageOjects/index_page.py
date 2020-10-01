# —— coding :utf-8 ——
# @time:    2020/10/1 3:38
# @IDE:     py_AppTest_Frameworkv1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    index_page.py
from Common.basepage import BasePage
class IndexPage(BasePage):
    def get_loginStatus(driver):
        # 获取当前app登录状态，已登录为True，未登录为False
        try:
            # 等待5秒，找登录/注册按钮
            return True
        except:
            return False