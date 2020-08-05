import unittest
from init import Test
from common.basepage import *
from page.baidu_page import *


class BaiduTest(Test, Baidu):

    def test_baidu_news_01(self):
        """百度新闻测试"""
        self.typenews()
        self.switch_to_front()
        self.assertEqual(self.get_current_url, Baidu.news_link)

    def test_baidu_map_02(self):
        """百度地图测试"""
        self.typemap()
        self.driver.get(Baidu.base_url)

    # @staticmethod
    # def suite(testclass):
    #     suite = unittest.TestLoader().loadTestsFromTestCase(testclass)
    #     return suite
#
if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(BaiduTest)  #unittest.makeSuite废弃不用了  加载测试类
    # unittest.TextTestRunner(verbosity=2).run(BaiduTest.suite(BaiduTest))
    unittest.main(verbosity=2)