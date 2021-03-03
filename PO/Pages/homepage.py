from public.basepage import BasePage
from selenium.webdriver.common.by import By


class Home(BasePage):
    url = 'http://121.196.12.97:9110/admin/index.html#/dashboard'
    click_text = (By.XPATH, '//i[@aria-label="图标: form"] /.. /..')
    write = (By.XPATH, '//a[@href="/posts/write"] /..')


    def click_txt(self):
        '''点击文章tab'''
        self.click(self.click_text)

    def write_txt(self):
        '''点击写文章'''
        self.click(self.write)

