# —— coding :utf-8 ——
# @time:    2020/10/1 3:39
# @IDE:     py_AppTest_Frameworkv1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    login_page.py
from Common.basepage import BasePage
from PageLocators.login_locator import LoginLocator as loc
class LoginPage(BasePage):
    '''登录页面类'''
    def input_username(self, username):
        # 输入用户名
        # 输入密码
        # 点击登录
        doc = "登录页面_输入用户名页面"
        self.Wait_eleVisible(loc.username_input, doc=doc)
        self.input_text(loc.username_input, username, doc)
        self.click_element(loc.next_step,doc)

    def input_password(self,password):
        doc = "登录页面_输入密码页面"
        self.Wait_eleVisible(loc.password_input, doc= doc)
        self.input_text(loc.password_input, password, doc)
        # 判断一下remembrance_user的来决定是否勾选
        self.click_element(loc.next_step, doc)

    # 获取错误提示信息 ----登录区域
    def get_errorMsg_from_userPage(self):
        doc = "登录页面_获取登录区域错误提示信息"
        self.Wait_eleVisible(loc.get_errorMsg_from_login, doc=doc)
        return self.get_eleText(loc.get_errorMsg_from_login, doc)

    # 获取错误提示信息---中间区域
    def get_errorMsg_from_passWordPage(self):
        doc = "登录页面_获取中间区域错误提示信息"
        self.Wait_eleVisible(loc.errorMsg_from_passWord, poll_frequency=0.2, doc=doc)  # 错误的密码和没有注册提示信息在中间区域显示
        return self.get_eleText(loc.errorMsg_from_passWord, doc)