1. py_AppTest_Frameworkv1.0目录架构
```
- Common        1.公共层
    - basepage          关键字封装(截图、异常处理、截图等功能)
    - dir_config        项目路径配置
    - logger            日志功能
- Desired_Caps  2. 固件层
    - desired_caps.yaml：设备信息、ip地址
- Outputs       3.输出层
    - Logs              过程日志
    - Reports           输出报告
    - Screenshots       错误日志截图
- PageObjects   4.页面元素层
- PageLoators   5.元素定位层
- TestCases     6.测试用例层
- TesstDatas    7.测试数据层
    - conftest          配置测试文件：测试前准备工作(连接服务器，进入登录状态)
- run.py主函数
```

2. basepage与web框架一样，新增的移动端方法：滑屏、toast获取、h5切换

3. 元素定位方式不同。新增移动端定位方式。
    - PageLoactors 全部换成移动端定位
    - 屏幕小，页面布局、页面功能有差异。页面变多
    - 页面划分时：登录页面-2个，考虑页面划分。
    
**4 .会话启动方式**
- web自动化：webdriver.Chrome()
- app自动化：
  1)提供平台和app信息：平台版本、平台名称、设备名称、app包名、app入口activity
  2）与appium服务进行连接，并发送平台和app信息
- toast信息：automationName = UiAutomator2
- noRest = True,False
 
- 使用yaml管理启动参数
- 定义 basedriver函数，启动与app的会话，可以在basedriver中定制启动参数

- 考虑：登录页面、登录成功、手势设置
- 原则：尽量不依赖app的状态和环境。在任何情况下都是可以执行的

5. 待优化：
    1. 通过adb命令获取当前连接的设备信息。平台版本、设备名称，设备id
        然后放到webdriver
    2. 多机并行执行 
        - 若要多设备并发，同时执行自动化测试，那么需要：
            确定设备个数
            每个设备对应一个 appium server 的端口号，并启动 appium
            pytest 要获取到每个设备的启动参数，然后执行自动化测试。  
        - 实现策略
            第一步：从设备池当中，获取当前连接的设备。若设备池为空，则无设备连接。
            第二步：若设备池不为空，启动一个线程，用来启动appium server.与设备个数对应。起始server端口为4723，每多一个设备，端口号默认+4
            第三步：若设备池不为空，则启用多个线程，来执行app自动化测试。
            
            
run.py文件
```
import unittest

import pytest
import os
from HTMLTestRunnerNew import HTMLTestRunner
from Common.dir_config import *

# 实例化套件对象
s = unittest.TestSuite()
# TestLoader用法：
    # 1. 实例化TestLoader对象
    # 2. 使用discover去找到一个目标下的所有测试用例
    # 3. 使用s
loader = unittest.TestLoader()
s.addTests(loader.discover(TestCases_dir))
# 运行
# runner = unittest.TextTestRunner()
# runner.run(s)


if __name__ =='main':
    pytest.main(["-m","smoke"]) # pytest -m smoke
```

