from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class Webdriver(object):
    def __init__(self, driver):
        self.driver = driver

    def findElement(self,*loc):
        """单个元素定位方法"""
        try:
            return WebDriverWait(self.driver,20).until(lambda x:x.find_element(*loc))
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))

    def findElements(self,*loc):
        """多个元素定位方法"""
        try:
            return WebDriverWait(self.driver,20).until(lambda x:x.find_elements(*loc))
        except NoSuchElementException as e:
            print('Error Details {0}'.format(e.args[0]))