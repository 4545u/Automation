from selenium.webdriver.common.by import By
from common.basepage import *


class Baidu(Webdriver):
        news_loc = (By.XPATH, '//*[@id="s-top-left"]/a[1]')
        map_loc = (By.XPATH, '//*[@id="s-top-left"]/a[3]')
        news_link = ('http://news.baidu.com/')
        map_link = ('https://map.baidu.com/@13428015,3656527,13z')
        base_url = ('https://www.baidu.com/')

        def typenews(self):
            self.findElement(*self.news_loc).click()

        def typemap(self):
            self.findElement(*self.map_loc).click()

        # @property
        # def get_handlers(self):
        #     return self.driver.window_handles

        def switch_to_front(self):
            handlers = self.driver.window_handles
            self.driver.switch_to_window(handlers[1])

        @property
        def get_current_url(self):
            return self.driver.current_url

