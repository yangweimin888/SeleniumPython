# -*- coding:utf-8 -*-
# @Time   : 2019-01-18 13:58
# @Author : YangWeiMin
import os
import yaml

class GetEmailParameter(object):

    def __init__(self):
        cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.email_path = os.path.join(os.path.join(cur_path, 'config'), 'email.yaml')
        if not os.path.exists(self.email_path):os.mkdir(self.email_path)


    def email_parameter(self):
        """获取email的配置信息"""
        with open(self.email_path, 'r', encoding='utf-8') as f:
            parameter = yaml.load(f)
        return parameter
