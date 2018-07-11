import os
from utils.file_reader import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH,'config','config.yml')
DATA_PATH = os.path.join(BASE_PATH,'data')
DRIVER_PATH = os.path.join(BASE_PATH,'drivers')
LOG_PATH = os.path.join(BASE_PATH,'log')
REPORT_PATH = os.path.join(BASE_PATH,'report')

class Config(object):
    '''Config 获取Yaml中的内容'''
    def __init__(self,config_file=CONFIG_FILE):
        self.config = YamlReader(config_file).data

    def get(self,element,index=0):
        '''可以配置很多参数，通过element以key_values形式调用'''
        return self.config[index].get(element)