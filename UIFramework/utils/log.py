import logging
import os
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH,Config


class Logger(object):
    def __init__(self,logger_name='framework'):
        '''设置log等级'''
        self.logger = logging.getLogger(logger_name)#初始化，与后面的%(name)s对应
        logging.root.setLevel(logging.NOTSET)       #日志级别NOTSET<DEBUG<INFO<WARNING<ERROR<CRITICAL
        log = Config().get('log')
        self.log_file_name = log.get('file_name') if log and log.get('file_name') else 'case.log'
        self.back_count = log.get('back_count') if log and log.get('back_count') else 5
        self.console_output_level = log.get('console_output_level') if log and log.get('console_output_level') else 'WARNING'
        self.file_output_level = log.get('file_output_level') if log and log.get('file_output_level') else "DEBUG"
        formatter = log.get('formatter') if log and log.get('formatter') else '%(asctime)s-%(name)s-%(levelname)s-%(message)s'
        self.formatter = logging.Formatter(formatter)

    def get_logger(self):
        '''设置控制台和log文件打印log等级'''
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH,self.log_file_name),   #加法方式path要有/
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.back_count,
                                                    encoding='utf-8',
                                                    delay=True)
            #print(LOG_PATH+self.log_file_name)
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger
logger = Logger().get_logger()
