from public.log import Log
from selenium import webdriver
from chromeoptions.ChromeOptions import Options

log = Log()


def open_browser(browser_type):
    # 添加异常处理机制 增加代码的健壮性
    try:
        if browser_type == "Chrome":
            log.info("chrome浏览器启动中")
            driver = webdriver.Chrome(options=Options().conf_option())
        else:
            log.info("非chrome浏览器启动中")
            driver = getattr(webdriver, browser_type)()
    except:
        log.info("未识别到浏览器对象，默认调用Chrome浏览器")
        driver = webdriver.Chrome(options=Options().conf_option())
    return driver


class Browser():

    def __init__(self, broweser_type):
        '''初始化浏览器，推荐使用Chrome浏览器'''
        self.driver = open_browser(broweser_type)
        self.driver.implicitly_wait(10)
