# -*- coding:utf-8 -*-
# @Time   : 2019-01-15 20:05
# @Author : YangWeiMin
import unittest
from page.LoginPage import Login
import time
from common.logger import Log


class TestCase(Login, unittest.TestCase):
    logger = Log('TestCase').get_log()

    def test_01(self):
        """正常登录"""
        self.switch_to_frame(0)
        self.account_login_page()
        time.sleep(5)
        self.input_tenantname()
        self.input_username()
        self.input_password()
        self.click_login()
        self.logger.info('登录成功')


if __name__ == '__main__':
    unittest.main()