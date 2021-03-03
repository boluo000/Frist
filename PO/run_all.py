# -*- coding: UTF-8 -*-
import os
import unittest

from public.mail import Send_Mail as mail
from unittestreport import TestRunner
import time

# 加载套件
def run():
    '''此主函数入口采用了线程的运行方式，使用了 TestRunner运行器,直接导包安装即可'''
    #根目录
    root_path = os.path.dirname(os.path.abspath(__file__))
    #测试用例路径
    test_path = os.path.join(root_path, 'testcase')
    #测试报告路径
    report_path = os.path.join(root_path, 'report', 'testreport')
    #测试报告名称
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    file_name = os.path.join(report_path, 'TestResult{}.html'.format(now))

    #用例执行路径
    suite = unittest.defaultTestLoader.discover(start_dir=test_path, pattern='test*.py')

    # 执行用例
    runner = TestRunner(suite,
                        filename=file_name,
                        report_dir=report_path,
                        title='测试报告',
                        tester='谢聪',
                        desc="谢聪执行测试生产的报告",
                        templates=1
                        )
    # 指定三个线程运行测试用例
    runner.run(thread_count=3)
    mail().send_mail()


if __name__ == '__main__':
    run()