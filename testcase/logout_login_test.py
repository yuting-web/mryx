# -*- coding: utf-8 -*-
# @Time : 2020/10/16 23:20
# @Author : 墨
# @Email : xgtlz@gmail.com
# @File : logout_login_test.py
# @Project : mryx
from page.base_page import BasePage
from page.mys_set_page import MysSetPage
from testcase.base_case import BaseCase
from page.mys_page import MysPage
from time import sleep
import unittest
from appium.webdriver.common.mobileby import MobileBy as By

class LogoutLogingTest(BaseCase):
    """注销登录测试"""
    def setUp(self) -> None:
        print("开始")
    def tearDown(self) -> None:
        # self.driver.quit() #退出App
        print("结束")

    def test_MRYX_ST_usr_002(self):
        """注销登录测试"""
        bp = BasePage(self.driver)
        sleep(5)
        bp.click((By.ID,"cn.missfresh.application:id/mineTab")) #点击我的
        sleep(1)
        bp.to_up(duration=3000) # 上滑出现设置
        mp = MysPage(self.driver) #实例化"我的"界面
        mp.click_set() #点击设置按钮
        sleep(1)
        msp = MysSetPage(self.driver) #实例化我的设置界面
        msp.click_sign_out() # 点击退出登录
if __name__ == '__main__':
    unittest.main()
