import unittest
from init import Test
from page.baidu_page import *


class BaiduTest(Test,Baidu):

    def test_baidu_01(self):
        """百度新闻"""
        self.typenews()
        self.switch_to_front()
        self.assertEqual(self.get_current_url, Baidu.news_link)

    def test_baidu_02(self):
        """百度地图"""
        self.typemap()
        self.driver.get(Baidu.base_url)


if __name__ == '__main__':
    # suite=unittest.TestSuite()  #实例化suite
    # suite.addTest(BaiduTest('baidu_news'))  #使用addTest方法，把测试用例添加到测试套件中
    # suite.addTest(BaiduTest('baidu_map'))
    # unittest.TextTestRunner(verbosity=2).run(suite)  #执行suite
    unittest.main(verbosity=2)
