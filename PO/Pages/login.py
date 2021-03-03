from public.basepage import BasePage
from selenium.webdriver.common.by import By


class Login(BasePage):
    url = 'http://121.196.12.97:9110/admin'
    uesr = (By.XPATH, '//input[@placeholder="用户名/邮箱"]')
    pwd = (By.XPATH, '//input[@placeholder="密码"]')
    button = (By.XPATH, '//span[contains(text(),"登 录")] /..')
    # 断言元素
    asr = (By.XPATH, '//span[contains(text(),"仪表盘")]')

    # button =(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/form/div[3]/div/div/span/button')

    def input_user(self, text):
        '''输入账户名'''
        self.send_keys(self.uesr, txt=text)

    def input_pwd(self, text):
        '''输入密码'''
        self.send_keys(self.pwd, txt=text)

    def login_button(self):
        '''点击登录按钮'''
        self.click(self.button)

    def ast(self,txt):
        '''文本断言'''
        result = self.assert_text(self.asr,expect=txt)
        if result == True:
            print('断言成功')
        else:
            print('断言失败')
