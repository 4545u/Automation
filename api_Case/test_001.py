import os
import time
import unittest
import requests
import json
import pymysql.cursors
from ddt import ddt,data,unpack
from common.read_excel import ExcelUnit


def connmysql():
    """连接mysql数据库"""
    con = pymysql.connect(host='119.45.55.114',user='root',passwd='199645',db='test')
    return con

def test_get_many():
    con = connmysql()
    cursor = con.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    print('查询的结果')
    for item in cursor.fetchall():
        print(item)
    print('共找出',cursor.rowcount,'条数据')
    cursor.close()
    con.close()

def test_get_one():
    con = connmysql()    #实例化connmysql方法
    cursor = con.cursor()    #获取游标
    sql = "select * from user where phone=%s and username=%s"  #写sql
    params = (15262424148,15262424148)    #条件参数，按顺序写
    cursor.execute(sql, params)          #用游标执行sql
    print('查询结果为：',cursor.fetchone())
    cursor.close()      #关闭游标
    con.close()         #关闭数据库

def test_insert_one():
    con = connmysql()
    cursor = con.cursor()
    sql = "insert into wx_user values (%s, %s, %s, %s, %s, %s)"
    params = (117,'fxk','fxp',117 ,'fxp','fxk')
    cursor.execute(sql, params)
    con.commit()
    cursor.close()
    con.close()

def test_insert_more():
    con = connmysql()
    cursor = con.cursor()
    sql = "insert into wx_user values (%s, %s, %s, %s, %s, %s)"
    params = [(119,'fxk','fxp',119 ,'fxp','fxk'),
              (118,'fxk','fxp',118 ,'fxp','fxk')]
    cursor.executemany(sql, params)
    con.commit()
    cursor.close()
    con.close()

if __name__ == '__main__':
    test_get_many()
    test_get_one()
    test_insert_one()
    test_insert_more()

