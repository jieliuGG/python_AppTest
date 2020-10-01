# —— coding :utf-8 ——
# @time:    2020/9/30 15:49
# @IDE:     py_AppTest_Frameworkv1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    basepage.py
import logging
import time
import datetime
from Common import dir_config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    # 等待元素可见
    def Wait_eleVisible(self,locator,timeout=30,poll_frequency=0.5,doc=''):
        """

        :param locator: 元素定位，元组形式。 格式：(元素类型,元素定位方式)
        :param timeout: 超时
        :param poll_frequency: 查找时睡眠间隔时间，默认0.5s
        :param doc:模块名称_页面名称_操作名称
        :return:
        """

        logging.info('等待元素{}可见'.format(locator))
        try:
            # 开始等待时间点
            start_time = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_frequency,doc).until(EC.visibility_of_element_located(locator))
            # 结束等待时间点
            end_time = datetime.datetime.now()
            # 等待时间，转换为秒
            wait_times = (end_time-start_time).seconds
            logging.info("{0}:元素:{1}已可见，等待起始时间：{2}，等待结束时间：{3}，等待时间：{4}".format(doc, locator, start_time, end_time, wait_times))
        except:
            # 捕获异常到指定目录
            logging.exception('等待元素可见异常')
            self.save_screenshot(doc)
            raise
    # 等待元素是否存在
    def Wait_ele_isExist(self,locator,timeout=30,doc=''):
        logging.info('{}中等待元素：{}是否存在'.format(doc,locator))
        try:
            WebDriverWait(self.driver,timeout,doc).until(EC.visibility_of_element_located(locator))
            logging.info('{0}秒内{1}存在元素：{2}'.format(timeout,doc,locator))
        except:
            logging.exception('{0}内{1}不存在元素：{2}'.format(timeout,doc,locator))
            self.save_screenshot(doc)
            raise
    # 查找元素
    def get_element(self,locator,doc=''):
        logging.info('{0}查找元素：{1}'.format(doc,locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception('{1}查找元素：{1}失败'.format(doc,locator))
            self.save_screenshot(doc)
            raise
    # 点击元素
    def click_element(self,locator,doc=''):
        ele = self.get_element(locator)
        logging.info('{}点击元素：{}'.format(doc,locator))
        try:
            ele.click()
        except:
            logging.exception('{0}点击元素：{1}失败'.format(doc,locator))
            self.save_screenshot(doc)
            raise
    # 输入操作
    def input_text(self,locator,text,doc=''):
        ele = self.get_element(locator)
        logging.info('{}元素：{}，输入内容为：{}'.format(doc,locator,text))
        try:
            ele.send_keys(text)
        except:
            logging.exception('元素输入操作失败')
            self.save_screenshot(doc)
            raise

    # 获取元素文本
    def get_eleText(self,locator,text,doc=''):
        ele = self.get_element(locator)
        logging.info("{0}获取元素：{1}的文本内容".format(doc, locator))
        try:
            text = ele.text
            logging.info('元素：{0}的文本内容为：{1}'.format(locator,text))
            return text
        except:
            logging.exception('元素：{0}获取文本内容失败'.format(locator))
            self.save_screenshot(doc)
            raise

    # 获取元素属性
    def get_ele_attribute(self,locator,attribute,doc=''):
        ele = self.get_element(locator)
        logging.info('{0}获取元素：{1}的属性：{2}'.format(doc,locator,attribute))
        try:
            ele_attr = ele.get_attribute(attribute)
            logging.info('获取元素：{0}的属性：{1}值为：{1}'.format(locator,attribute,ele_attr))
            return ele_attr
        except:
            logging.exception('获取元素：{0}属性：{1}属性值失败'.format(locator,attribute))
            self.save_screenshot(doc)
            raise

    # toast获取   toast信息：automationName = UiAutomator2
    def get_toastMsg(self, str):
        # 1. xpath表达式，文本匹配
        loc = '//*[contains(@text,"{}")]'.format(str)
        # 等待时用元素存在的条件，不能用元素可见条件
        try:
            WebDriverWait(self.driver,10,0.01).until(EC.visibility_of_element_located((MobileBy.XPATH,loc)))
            return self.driver.find_element_by_xpath(loc).text
        except:
            logging.exception('没有找到匹配的toast！')
            raise
    # alert处理
    def aler_action(self,locator,doc=''):
        ele = self.get_element(locator,doc)
        logging.info('{0}元素：{1}关闭弹出框操作'.format(doc,locator))
        # 关闭弹框
        try:
            ele.close()
        except:
            logging.exception('{}弹出框关闭操作失败'.format(doc))
            self.save_screenshot(doc)
            raise
    # 获取整个屏幕大小
    def get_size(self):
        return self.driver.get_window_size()

    # 上下左右滑动
    def swipe_up(self):
        size = self.driver.get_window_size()
        self.driver(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.1)

    def swipe_down(self):
        size = self.driver.get_window_size()
        self.driver(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5, size["height"] * 0.9)

    def swipe_left(self, size):
        size = self.driver.get_window_size()
        self.driver(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5)

    def swipe_right(self):
        size = self.driver.get_window_size()
        self.driver(size["width"] * 0.1, size["height"] * 0.5, size["width"] * 0.9, size["height"] * 0.5)

    # 保存截图
    def  save_screenshot(self,doc):
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        filepath = dir_config.screenshots_dir+\
                   r'\{0}_{1}.png'.format(doc,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(filepath)
        try:
            return self.driver.save_screenshot(filepath)
        except:
            logging.exception('{}截图失败'.format(doc))
            raise


