# —— coding :utf-8 ——
# @time:    2020/9/30 15:50
# @IDE:     py_AppTest_Frameworkv1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    logger.py
import logging
from logging.handlers import RotatingFileHandler
import time
from Common import dir_config

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

handler_2 = RotatingFileHandler(dir_config.logs_dir+"/Web_Autotest_{0}.log".format(curTime),backupCount=20,encoding='utf-8')

#设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])