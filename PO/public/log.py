import logging
import os
import time


class Log:

    def __init__(self):
        '''初始化日志文件路径
            root_path: Log.py文件所在的文件目录 == POframework/log,可以理解为根目录
            self.logname:拼接文件目录，设置日志文件输出地址
        '''
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.logname = os.path.join(root_path,'report','log','{0}.log'.format(time.strftime('%Y-%m-%d')))

        #以__开头的函数 私有函数，只有内部的类对象可以访问，子类和外部对象都不可以访问该函数
    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #格式化日志文件和控制台输出信息
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler记录器里面
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)


if __name__ == '__main__':
    # root_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    # print(os.path.join(root_path,'report','log','{0}.log'.format(time.strftime('%Y-%m-%d'))))
    log =Log()
    log.info('测试')












