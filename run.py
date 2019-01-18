# -*- coding:utf-8 -*-
# @Time   : 2018-11-01 19:21
# @Author : YangWeiMin
import os
import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from common.logger import Log
from common.get_email_parameter import GetEmailParameter

"""
执行用例并发送报告，分四个步骤:
第一步：加载用例
第二步：执行用例
第三步：获取最新的测试报告
第四步：发送邮件
"""


# 获取当前脚本的真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log = Log('run').get_log()

def add_case(caseName='case', rule='test*.py'):
    '''
    作用：加载所有测试用例
    :param caseName:
    :param rule:
    :return:
    '''
    case_path = os.path.join(os.getcwd(), caseName)
    if not os.path.exists(case_path):os.mkdir(case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover

def run_case(all_case, reportName='reports'):
    '''
    作用：执行所有的用例，并把执行结果写入HTML测试报告中
    :param all_case:
    :param reportName:
    :return:
    '''
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    report_path = os.path.join(cur_path, reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now + 'result.html')
    with open(report_abspath, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='外勤365web自动化测试报告', description='用例执行情况')
        runner.run(all_case)


def get_report_file(report_path):
    '''
    作用: 获取最新的测试报告
    :param report_path:
    :return:
    '''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path, fn)))
    print('最新测试报告：' + lists[-1])
    # 找到最新的测试报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(subject, sender, psw, receiver, smtpserver, report_file, port):
    """
    作用：将最新的测试报告通过邮件进行发送
    :param sender:发件人
    :param psw:QQ邮箱授权码
    :param receiver:收件人
    :param smtpserver:QQ邮箱服务
    :param report_file:
    :param port:端口
    :return:
    """
    with open(report_file, 'rb') as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = subject
    msg['from'] = sender
    msg['to'] = ','.join(receiver)
    msg.attach(body)

    # 添加附件
    att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名和密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    log.info('测试报告邮件发送成功')

if __name__ == '__main__':
    # 加载用例
    all_case = add_case()
    # 执行用例
    run_case(all_case)
    # 获取最新的测试报告
    report_path = os.path.join(cur_path, 'reports')
    report_file = get_report_file(report_path)
    # 邮箱配置
    subject = GetEmailParameter().email_parameter()['subject']
    sender = GetEmailParameter().email_parameter()['sender']
    psw = GetEmailParameter().email_parameter()['psw']
    smtp_server = GetEmailParameter().email_parameter()['smtp_server']
    port = GetEmailParameter().email_parameter()['port']
    receiver = GetEmailParameter().email_parameter()['receiver'].split(',')
    send_mail(subject, sender, psw, receiver, smtp_server, report_file, port)