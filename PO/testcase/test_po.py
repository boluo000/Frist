import time
from public.log import Log
import unittest
from Pages.login import Login
from Pages.homepage import Home
from public.browser import Browser

log = Log()


class Testdemo(unittest.TestCase):
    def setUp(self):
        self.browser = Browser(broweser_type='Chrome')

    def tearDown(self):
        time.sleep(5)
        self.browser.driver.quit()

    def test_01(self):
        lp = Login(self.browser,Login.url)
        lp.visit()
        lp.input_user('菠萝')
        log.info('账户输入成功')
        lp.input_pwd('xiecong000')
        log.info('密码输入成功')

        lp.login_button()
        log.info("登录点击成功")
        # lp.ast('仪表盘')    #这个是自己写的断言方法
        self.assertTrue(lp.assert_text(Login.asr,'仪表盘'))  #这个是unittest自带的断言方法
        hp = Home(self.browser,Home.url)
        hp.visit()
        hp.click_txt()
        log.info('点击文章tab')
        hp.write_txt()
        log.info('点击写文章')





if __name__ == '__main__':
    unittest.main()
