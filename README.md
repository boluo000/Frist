# PO框架文档解析

### 一：模块介绍

```sh
chromeOptions:
这个模块主要是存放chrome浏览器的配置类

config:
这个模块主要是存放邮件相关的配置信息，可通过对配置文件修改实现对不同的人发送测试邮件

pages:
这个模块主要存放业务流程的页面对象

public:
这个属于公共类
baseoage: 底层代码 页面对象的基类
browser: 浏览器的判断以及实例化
HTMLTestRunner: 结合unittest的运行器，并生成测试报告
log:日志模块
mail:邮件发送模块
readconfig:配置文件读取

report:
img:存放测试用例报错的截图
log:存放执行测试用例产生的系统日志
testreport:存放测试报告

testcase
测试用例存放模块

run_all:主函数入口 这个函数采用了 多线程的方式进行执行测试用例，会把每个py测试文件当成一个线程去启动，可以在该函数里调整线程个数，这个函数使用了 TestRunner运行器 直接 from unittestreport import TestRunner即可

run:主函数入口，这函数入口没有采用多线程的方式执行，执行效率偏慢,使用的是HTMLTestRunner运行器

注意事项：
1：测试用例的py文件必须以test为开头，否者多线程的测试用例是将无法识别
2：测试用例编写 必须使用unittest框架编写测试用例，在setUp函数里面必须要初始化浏览器对象即：self.browser = Browser(broweser_type='Chrome') 建议使用chrome浏览器，如果使用其他浏览器将不能获的浏览器配置。如果需要火狐的浏览器配置，可在配置模块添加 然后修改browser模块 添加进去配置即可。

新增：
修复了底层代码的一些小bug 底层代码添加了断言方法



```

