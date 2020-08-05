from selenium.webdriver.common.by import By
from common.basepage import *
from common.read_excel import *


def sina_login_date():
    date = ExcelUnit.read_excel_port('E://git//Automation//test_file//ui_case.xlsx', 'Sheet1', 2, 4, 1, 3)
    return date

class sina(Webdriver):
    username_loc = (By.XPATH, '//*[@id="freename"]')
    password_loc = (By.XPATH, '//*[@id="freepassword"]')
    login_loc = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[7]/div[1]/a[1]')
    loginError_loc = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]')

    def typeusername(self,username):
        self.findElement(*self.username_loc).send_keys(username)

    def typepassword(self,password):
        self.findElement(*self.password_loc).send_keys(password)


    def clicklogin(self):
        self.findElement(*self.login_loc).click()

    @property
    def getloginError(self):
        return self.findElement(*self.loginError_loc).text

    def sina_login(self,username,password):
        self.typeusername(username)
        self.typepassword(password)
        self.clicklogin()





