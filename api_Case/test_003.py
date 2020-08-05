"""流程：需求分析-用例设计-脚本开发-测试执行-结果分析"""
# 1.获取接口文档：请求方式 传输协议 请求参数 响应参数 判断测试是否通过测试用例
# 2.脚本开发，使用requests模块进行接口调用
#     request包含内容：
#         1.封装各种请求类型，get,post等
#         2.以关键字参数的方式，封装了各种请求参数，params,data,headers,token等
#         3.封装了响应内容，status_code,json(),cookies,url等
#         4.session会话对象，可以跨请求
# 3.使用unittest执行测试，编写断言进行结果校验
# 4.发送邮件报告
# 5.结合测试报告进行结果分析

# 数据校验
# 1.连接数据库，操作数据库
# 2.testsql.py写查询sql，数据校验（断言sql查询与api返回校验）
# 3.testapi测试接口


import requests,json
import unittest

class Api(unittest.TestCase):

    def statuscode(self,r):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['msg'],'ok')

    def api_url(self):
        return 'http://api.hsgchina.com/'
        #return 'http://api.pre.hsgchina.com/'

    def test_001(self):
        data = {
            'username':'18351113929',
            'password':'123qwer'
        }
        r = requests.post(self.api_url() + 'public/oauth/signin',data=data)
        with open('token','w') as f:
            f.write(r.json()['data']['accessToken'])
        self.statuscode(r=r)

    def get_token(self):
        with open('token','r') as f:
            return f.read()

    def test_002(self):
        params = {
            'currentPage':'0',
            'pageSize':'10',
            '0':'status',
            'Access-Token':self.get_token()
        }
        r = requests.get(self.api_url() + 'app/orders/list',params=params)
        self.statuscode(r=r)

    def test_003(self):
        params = {
            'type':'1',
            'Access-Token':self.get_token()
        }
        r = requests.get(self.api_url() + 'app/withdrawal/detail',params=params)
        self.statuscode(r=r)

if __name__ == '__main__':
    unittest.main(verbosity=2)

