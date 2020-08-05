import unittest
import os, time
from BeautifulReport import BeautifulReport
# from common.sendemail import SendEmail


if __name__ == '__main__':
    test_reports_address = './report'  #测试报告存放的位置
    discover = unittest.defaultTestLoader.discover(os.path.dirname(__file__), 'test*.py', None)
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = '测试报告' + str(now)   #报告名字
    BeautifulReport(discover).report(description='测试', filename=filename, report_dir='report')
    """发送邮件，有问题。。。"""
    # time.sleep(6)
    # new_report_addr = SendEmail().acquire_report_address(test_reports_address)
    # SendEmail().send_email(new_report_addr)
