import unittest
import time,os
from utils.mail import Email
from utils.config import Config,REPORT_PATH,DATA_PATH,LOG_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from test.page.baidu_result_page import BaiDuResultPage,BaiDuMainPage
from utils.HTMLTestRunner_PY3 import HTMLTestRunner


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = os.path.join(DATA_PATH , 'baidu_search.xlsx')

    def sub_setUp(self):
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL)
    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        '''对小心走火、小坦克、jianhao_he执行百度搜索操作'''
        datas = ExcelReader(excel=self.excel).data

        for d in datas:
            print(d)
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['A'])
                self.page = BaiDuResultPage(self.page)
                links = self.page.result
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__=="__main__":
    times = time.strftime('%Y%m%d%H',time.localtime())
    report = os.path.join(REPORT_PATH,'report'+times+'.html')
    print(report)
    # log = Config().get('file_name')
    # print(log)

    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,description='baidusousuo',title='automation test report')
        runner.run(TestBaiDu('test_search'))

    e = Email(sender='13661501664@163.com',
              password='yyy0909',
              receiver='16602104373@163.com',
              path=report,
              server='smtp.163.com',
              title='自动化测试报告',
              message='python youjian ')
    e.send()