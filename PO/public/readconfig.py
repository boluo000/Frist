#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:读取配置文件
 @author: yansh
"""
import os
import sys
import configparser
import codecs
'''
os.path.abspath(__file__) 作用： 获取当前脚本的完整路径
'''
#获得conf.ini的文件路径
conf_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\config\\config.ini'
#返回当前文件所在的目录
root_path = os.path.dirname(os.path.abspath(sys.argv[0]))
# conf_path=os


class ReadConfig:
    """
    专门读取配置文件的，.ini文件格式
    """

    def __init__(self, filename=conf_path):
        # configpath = filename
        with open(filename, 'r', encoding='UTF-8') as f:
            # f = open(configpath, encoding='UTF-8')
            data = f.read()
            # remove BOM  BOM_UTF8 = b'\xef\xbb\xbf' 切片去掉\xef\xbb\xbf，只留下b''
            if data[:3] == codecs.BOM_UTF8:
                data =  data[3:]
                files = codecs.open(filename, "w")
                files.write(data)
                files.close()
            # fd.close()

        #文件类型解析
        self.cf = configparser.ConfigParser()
        self.cf.read(filename, encoding='UTF-8')  # read(file_path, encoding='UTF-8'), 如果代码有中文注释，用这个，不然报解码错误

    def get_value(self, env, name):
        """读取配置文件中的值"""
        return self.cf.get(env, name)



if __name__ == '__main__':
    # ReadConfig.getValue()
    print(conf_path)