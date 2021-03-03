import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from public.log import Log
from public.readconfig import ReadConfig
import os



log = Log()
readconf = ReadConfig()

#返回路径为 D:\PO
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#配置测试报告路径
report_path = os.path.join(root_path,'report','testreport')
mail_server = readconf.get_value('Mail', 'mail_server')
mail_subject = readconf.get_value('Mail', 'mail_subject')

#配置收件人
recvaddress = readconf.get_value('Mail', 'mail_to')  # ['xxx.xx@xxx.com', 'xxxx@qq.com']
sendaddr_name = readconf.get_value('Mail', 'mail_from')
sendaddr_pwd = readconf.get_value('Mail', 'mail_from_pwd')



class Send_Mail:

    def __init__(self,recver=None):
        if recver is None:
            self.Send_to = recvaddress
        else:
            self.Send_to = recver

    def __get_report(self):
        '''获取最新的测试报告'''
        reportdir = os.listdir(os.path.abspath(report_path))
        reportdir.sort()
        #获取文件的最后一个测试报告 也就是最新的测试报告
        newreportname = reportdir[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_message(self):
        '''生成邮件的内容和html的测试报告附件'''
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = mail_subject
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(report_path,newreport),'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    def send_mail(self):
        '''发送邮件'''
        log.info('开始发送邮件')
        self.__take_message()
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP(mail_server, 25)
            smtp.login(sendaddr_name, sendaddr_pwd)
            smtp.sendmail(self.msg['from'], self.Send_to, self.msg.as_string())
            smtp.close()
            log.info('邮件发送成功！！')
        except Exception as e:
            log.error('发送邮件错误,{}'.format(e))
            raise

if __name__ == '__main__':
    Send_Mail().send_mail()


















