import os, sys
import time
import unittest
from public import HTMLTestRunner
from public.log import Log
from public.mail import Send_Mail as mail

log = Log()
root_path = os.path.dirname(os.path.abspath(__file__))
# print(root_path)
# root_path = os.path.dirname(os.path.abspath(sys.argv[0]))

def run():
    test_path = os.path.join(root_path, 'testcase')
    # print(test_path)
    suite = unittest.defaultTestLoader.discover(start_dir=test_path, pattern='test*.py')
    report_path = os.path.join(root_path, 'report', 'testreport')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    report_name = os.path.join(report_path, 'TestResult{}.html'.format(now))
    # report_name = report_path + '\\' + 'TestResult' + now + '.html'
    with open(report_name, 'wb') as f:  # encoding='UTF-8'
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    mail().send_mail()


if __name__ == '__main__':
    run()

