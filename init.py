import unittest
from selenium import webdriver
# from page.basepage import *
from selenium.webdriver.chrome.options import Options
from common.url import *


class Test(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        # chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
        chrome_options.add_argument("start-maximized")                     # 浏览器最大化
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')  # 取消沙盒模式，解决DevToolsActivePort文件不存在的报错
        # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        # chrome_options.add_argument('--headless')                          # 无头模式启动
        chrome_options.add_argument('--disable-gpu')                       #
        # chrome_options.add_argument('start-fullscreen')                    #浏览器全屏
        # chrome_options.add_argument('disable-infobars')                    #关闭浏览器信息
        # self.driver = webdriver.Chrome("/usr/local/share/chromedriver",chrome_options=chrome_options)   #Linux
        self.driver = webdriver.Chrome("C:\Python37\Scripts\chromedriver",chrome_options=chrome_options)   #win
        # self.driver = webdriver.Chrome()
        # self.page = (self.driver)
        self.driver.get(url.base_url)
        # self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()


