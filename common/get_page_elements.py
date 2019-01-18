# -*- coding:utf-8 -*-
# @Time   : 2019-01-18 10:09
# @Author : YangWeiMin
import yaml
import os


class GetPageElements(object):

    def __init__(self, page_name):
        """拼接页面地址，如果不存在则自动创建"""
        self.page_name = page_name
        cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.page_path = os.path.join(os.path.join(cur_path, 'config'), self.page_name)
        if not os.path.exists(self.page_path):os.mkdir(self.page_path)


    def login_page_elements(self):
        """获取登录页面的页面元素"""
        with open(self.page_path, 'r', encoding='utf-8') as f:
            elements = yaml.load(f)
        return elements


