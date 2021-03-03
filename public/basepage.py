import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from public.log import Log
import time
from selenium.common.exceptions import NoSuchElementException

log = Log()


class BasePage(object):

    def __init__(self, browser, url):
        '''初始化driver对象'''
        self.driver = browser.driver
        self.url = url

    @staticmethod
    def isdisplayed(element):
        '''判断元素是否存在,并且将函数转换为静态函数，静态方法不会接受的隐式的第一个参数，只会绑定该函数的的参数'''
        value = element.isdisplayed()
        if value:
            log.info('元素存在'.format(element))
        else:
            log.info('元素不存在'.format(element))
        return value

    @staticmethod
    def time_wait(secondes):
        '''强制等待'''
        time.sleep(secondes)
        log.info('暂停%d秒' % secondes)

    def forword(self):
        '''页面前进'''
        self.driver.forward()
        log.info('当前页面页面点击前进')

    def back(self):
        '''页面后退'''
        self.driver.back()
        log.info('当前页面点击后退')

    def wait(self, seconed):
        '''建议隐式等待10s'''
        self.driver.implicitly_wait(seconed)
        log.info('隐式等待{0}s'.format(seconed))

    def get_img(self, rq=time.strftime('%Y%m%d%H%M', time.localtime(time.time()))):
        """截图,os.path.abspath('..'):返回根目录"""
        path = os.path.join(os.path.abspath('..'), 'report', 'img', 'erro')
        # path = os.path.join(getcwd.get_cwd(), 'screenshots/')  # 拼接截图保存路径
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 按格式获取当前时间
        screen_name = path + rq + '.png'  # 拼接截图文件名
        # noinspection PyBroadException
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log.info("截图保存成功{}".format(screen_name))
        except BaseException as e:
            log.error("截图失败{}".format(e))

    # def locator(self, name, value):
    #     '''
    #     元素定位函数
    #     :param name:元素定位方法
    #     :param value: 元素定位的值
    #     :return:
    #     '''
    #     try:
    #         return self.driver.find_element(getattr(By, name.upper()), value)
    #     except NoSuchElementException as e:
    #         log.error('元素定位异常:'.format(e))
    #         self.get_img()

    def locator(self, *loc):
        '''以元组或列表的方式传递元素定位参数
            例如 (By.ID,'kw')
        '''
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            log.error('元素定位异常'.format(e))
            self.get_img()

    def wait_element_click(self, loc):
        '''
        显示等待
        等待元素出现后，立即点击该元素
        '''
        try:
            elment = WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(*loc),
                                                               message="\n元素等待超过10s,查找频率为0,5s，未定位到元素")
            elment.click()
            log.info('元素定位成功，元素点击成功')
        except Exception as e:
            log.error('未等待到元素出现，元素点击失败：{0}'.format(e))
            self.get_img()

    def wait_element(self, loc):
        '''
        显示等待
        等待元素出现后,返回该元素
        '''
        try:
            elment = WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.locator(*loc),
                                                               message="\n元素等待超过10s,查找频率为0,5s，未定位到元素")
            return elment
        except Exception as e:
            log.error('{0}'.format(e))

    def close(self):
        '''关闭浏览器，建议使用quit()函数退出浏览器'''
        try:
            self.driver.close()
            log.info('关闭浏览器成功')
        except NameError as e:
            log.error('浏览器关闭异常:{0}'.format(e))

    def quit(self):
        '''彻底退出浏览器'''
        try:
            self.driver.quit()
            log.info('浏览器退出成功')
        except NameError as e:
            log.error('浏览器退出异常:{0}'.format(e))

    def click(self, loc):
        '''元素点击'''
        try:
            self.locator(*loc).click()
        except Exception as e:
            log.error('元素点击异常:{0}'.format(e))
            self.get_img()

    def send_keys(self, loc, txt):
        '''输入文本内容'''
        try:
            self.locator(*loc).send_keys(txt)
        except Exception as e:
            log.error('文本输入异常:{0}'.format(e))
            self.get_img()

    def right_click(self, loc):
        '''右击元素'''
        try:
            # self.wait_element(*loc)
            el = self.locator(*loc)
            ActionChains(self.driver).context_click(el).perform()
            log.info('右击元素{}'.format(*loc[1]))
        except Exception as e:
            log.error('右击元素{}报错,{}'.format(*loc[1], e))
            raise

    def double_click(self, loc):
        """双击元素"""
        try:
            # self.wait_element(*loc)
            el = self.locator(*loc)
            ActionChains(self.driver).double_click(el).perform()
            log.info('双击元素{}'.format(*loc[1]))
        except Exception as e:
            log.error('双击元素{}错误'.format(*loc[1], e))
            raise

    def get_attribute(self, loc, attribute):
        """获取元素属性值"""
        try:
            # el = self.get_element(selector)
            el = self.locator(*loc)
            attr = el.get_attribute(attribute)
            log.info('获取元素{}的属性{}值为：{}'.format(*loc[1], attribute, attr))
            return attr
        except Exception as e:
            log.error('获取元素{}的属性{}值错误,{}'.format(*loc[1], attribute, e))
            raise

    def get_text(self, loc):
        '''获取元素文本内容'''
        try:
            text = self.locator(*loc).text
            log.info('获取元素{}的文本信息为：{}'.format(*loc[1], text))
            return text
        except Exception as e:
            log.error('获取元素{}的文本信息错误,{}'.format(*loc[1], e))
            raise

    def use_js(self, js):
        '''执行js语句'''
        try:
            self.driver.execute_script(js)
            log.info('执行%s语句成功' % js)
        except Exception as e:
            log.error('js语句执行异常'.format(e))

    def get_url(self):
        """获取url"""
        url = self.driver.current_url
        log.info('当前窗口的url为{}'.format(url))
        return url

    def visit(self):
        '''访问url'''
        try:
            self.driver.get(self.url)
            log.info('打开{0}成功'.format(self.url))
        except Exception as e:
            log.error('打开url异常'.format(e))

    def switch_menue(self, parentelement, secelement, targetelement):
        """三级菜单切换"""
        self.time_wait(3)
        # noinspection PyBroadException
        try:
            self.driver.switch_to.default_content()
            self.click(parentelement)
            log.info('成功点击一级菜单：%s' % parentelement)
            self.click(secelement)
            log.info('成功点击二级菜单：%s' % secelement)
            self.click(targetelement)
            log.info('成功点击三级菜单：%s' % targetelement)
        except BaseException as e:
            log.error('切换菜单报错:{0}'.format(e))

    def swicth_iframe(self, loc):
        '''切换iframe嵌套层'''
        element = self.locator(*loc)
        try:
            self.driver.switch_to.frame(element)
            log.info('frame切换成功')
        except Exception as e:
            log.error('frame切换异常:{0}'.format(e))

    def accept_alert(self):
        """确认报警框"""
        self.driver.switch_to.alert.accept()
        log.info('确认报警框')

    def dismiss_alert(self):
        """确认报警框"""
        self.driver.switch_to.alert.dismiss()
        log.info('拒绝报警框')

    def get_title(self):
        """获取title"""
        title = self.driver.title
        log.info('当前窗口的title为{}'.format(title))
        return title

    def open_new_window(self, loc):
        """在新的窗口打开链接"""
        try:
            original_windows = self.driver.current_window_handle
            el = self.locator(*loc)
            el.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle)
            log.info('点击元素{}在新窗口打开'.format(*loc[1]))
        except Exception as e:
            log.error('点击元素{}在新窗口打开错误,{}'.format(*loc[1], e))
            raise

    def into_new_window(self):
        """切换至新窗口"""
        # t1 = time.time()
        try:
            all_handle = self.driver.window_handles
            flag = 0
            while len(all_handle) < 2:
                time.sleep(1)
                all_handle = self.driver.window_handles
                flag += 1
                if flag == 5:
                    break
            self.driver.switch_to.window(all_handle[-1])
            log.info('切换至新窗口，新窗口url为{}'.format(self.driver.current_url))
        except Exception as e:
            log.error('切换至新窗口错误,{}'.format(e))
            raise

    def set_window(self, wide, high):
        """设置浏览器的宽 高"""
        # t1 = time.time()
        self.driver.set_window_size(wide, high)
        log.info('设置浏览器宽：{} 高：{}'.format(wide, high))

    def type_Enter(self, loc):
        """输入回车"""
        try:
            el = self.locator(*loc)
            el.send_keys(Keys.ENTER)
            log.info('输入回车')
        except Exception as e:
            log.error('输入回车错误,{}'.format(e))
            raise

    def F5(self):
        """刷新页面"""
        # t1 = time
        self.driver.refresh()
        log.info('刷新页面')

    def original_driver(self):
        """返回原生driver"""
        return self.driver

    def assert_text(self, loc, expect):
        '''断言机制：获取元素的文本信息，进行比对校验'''
        reality = self.locator(*loc).text
        if reality == expect:
            return True
        else:
            return False


if __name__ == '__main__':
    path = os.path.join(os.path.abspath('..'), 'report', 'img')
    print(path)
