# —— coding :utf-8 ——
# @time:    2020/9/30 15:49
# @IDE:     py_AppTest_Frameworkv1.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    dir_config.py
import os
base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 测试用例路径
TestCases_dir = os.path.join(base_path,'TestCases')

# 测试数据路径
TestDatas_dir = os.path.join(base_path,'TestDatas')

# 输出日志路径
logs_dir = os.path.join(base_path,'Outputs','logs')

# 输出报告路径
reports_dir = os.path.join(base_path,'reports')

# 截图路径
screenshots_dir = os.path.join(base_path,'screenshots')

if __name__ == '__main__':
    print(screenshots_dir)