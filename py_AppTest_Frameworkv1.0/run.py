import  unittest
import pytest
from Common.dir_config import *
# TestLoader用法：
    # 1. 实例化TestLoader对象
    # 2. 使用discover去找到一个目录下的所有测试用例
    # 3. 使用s

s = unittest.TestSuite()
loader = unittest.TestLoader()
s.addTests(loader.discover(TestCases_dir))
# runner = unittest.TextTestRunner()
# runner.run(s)

if __name__ == '__main__':
    pytest.main(['-m','smoke'])