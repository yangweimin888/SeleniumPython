# -*- coding:utf-8 -*-
# @Time   : 2019-01-15 19:04
# @Author : YangWeiMin

from page.BasePage import BasePage
from common.get_page_elements import GetPageElements
from common.get_environment_parameter import GetEnvironmentParameter


class Login(BasePage):
    """登录页面"""
    login_elements = GetPageElements('LoginPage.yaml').login_page_elements()
    account_login = ('xpath', login_elements['account_login'])
    tenantname_loc = ('id', login_elements['tenantname_loc'])
    username_loc = ('id', login_elements['username_loc'])
    password_loc = ('id', login_elements['password_loc'])
    login_button = ('id', login_elements['login_button'])


    def switch_to_frame(self, value):
        """进入iframe页面"""
        self.driver.switch_to.frame(value)


    def account_login_page(self):
        """进入账户登录页面"""
        self.click_button(self.account_login)


    def input_tenantname(self):
        """输入企业名"""
        self.click_button(self.tenantname_loc)
        self.clear_key(self.tenantname_loc)
        self.send_keys(self.tenantname_loc, self.parameter['tenantname'])


    def input_username(self):
        """输入用户名"""
        self.click_button(self.username_loc)
        self.clear_key(self.username_loc)
        self.send_keys(self.username_loc, self.parameter['username'])


    def input_password(self):
        """输入密码"""
        self.click_button(self.password_loc)
        self.clear_key(self.password_loc)
        self.send_keys(self.password_loc, self.parameter['password'])


    def click_login(self):
        self.click_button(self.login_button)