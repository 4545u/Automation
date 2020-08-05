from init import *
from ddt import ddt,data,unpack
from page.sina_page import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@ddt()
class sina_test(Test,sina):
    @data(*sina_login_date())
    @unpack
    def test_login(self, username, password, result):
        self.sina_login(username,password)
        self.assertEqual(self.getloginError,result)

if __name__ == '__main__':
    unittest.main(verbosity=2)