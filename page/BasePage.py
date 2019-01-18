# -*- coding:utf-8 -*-
# @Time   : 2019-01-15 16:21
# @Author : YangWeiMin

import time
from common.logger import Log
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium import webdriver
from common.get_environment_parameter import GetEnvironmentParameter


class BasePage(unittest.TestCase):
    """
    定义一个页面基类，让所有的页面都继承该类，封装一些常用的页面操作方法
    """
    logger = Log(logger='BasePage').get_log()
    parameter = GetEnvironmentParameter().environment_parameter('test')



    def setUp(self):
        self.logger.info('------开始执行测试用例------')


    @classmethod
    def setUpClass(cls):
        browser = input('please enter browser name:\n')
        if browser == 'firefox':
            cls.driver = webdriver.Firefox()
        elif browser == 'chrome':
            cls.driver = webdriver.Chrome()
        else:
            cls.logger.warning('browser name enter error......')
            pass
        cls.driver.get(cls.parameter['url'])
        cls.driver.maximize_window()


    def find_element(self, loc):
        """重写查找元素的方法"""
        try:
            WebDriverWait(self.driver, 15).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            self.logger.error('%s 页面中未能找到%s 元素' % (self, loc))


    def clear_key(self, loc):
        """重写清空文本框"""
        time.sleep(3)
        self.find_element(loc).clear()


    def send_keys(self, loc, value):
        """输入内容"""
        self.clear_key(loc)
        self.find_element(loc).send_keys(value)


    def click_button(self, loc):
        """点击按钮"""
        self.find_element(loc).click()



if __name__ == '__main__':
    unittest.main()