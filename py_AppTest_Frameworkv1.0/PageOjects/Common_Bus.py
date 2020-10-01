# —— coding :utf-8 ——
# @time:    2020/10/1 3:40
# @IDE:     py_AppTest_Frameworkv1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    Common_Bus.py
from Common.basepage import BasePage
import time
from appium.webdriver.common.touch_action import TouchAction
from PageLocators import Common_locator as Cloc
import logging
# 公共业务

# 欢迎页面
class CommonBus(BasePage):
    # 处理欢迎页面
    def handle_welcome_page(self):
        """
        如果没有找到首页元素/或不包含MainActivity，就是欢迎页面
        """
        time.sleep(7)
        curAct = self.driver.current_activity
        if curAct.find("MainActivity") == -1:  # 字符串找不到返回-1
            # 滑动欢迎页面至首页
            # 左滑三次，点击立即体验
            for i in range(3):
                self.swipe_left(self.get_size())
                time.sleep(1)
            # 点击立即体验

    # 导航页面

    # 是否设置手势密码
    def is_setGesture(self, action=False,a=None,b=None,c=None,d=None):
        # 有没有设置手势，密码的弹框 -5s
        # 如果有，是设置还是不设置
        if action == False: # 点击不设置
            try:
                self.click_element(Cloc.No_setGesture)
            except Exception as e:
                logging.exception(e)
                raise e
        else:  ##手势密码 封装： 九宫格（012；345；678）手势为：1478
            list_pwd = self.driver.find_elements_by_class_name("android.widget.ImageView")
            TouchAction(self.driver).press(list_pwd[a]).move_to(list_pwd[a]).move_to(list_pwd[b]).wait(100).move_to(
                list_pwd[c]).wait(100).move_to(list_pwd[d]).release().perform()
            time.sleep(1)
            print("输入手势密码")
            """如果为新注册，或者修改手势密码的时候，需要输入两次手势密码，如果只是登录的话就是一次"""
            try:
                ee = self.driver.find_element_by_name("请再绘制手势密码")
                list_pwd = self.driver.find_elements_by_class_name("android.widget.ImageView")
                TouchAction(self.driver).press(list_pwd[1]).move_to(list_pwd[1]).move_to(list_pwd[4]).wait(100).move_to(
                    list_pwd[7]).wait(100).move_to(list_pwd[8]).release().perform()
            except Exception:
                pass