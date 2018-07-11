import os
import time
from selenium import webdriver
from utils.config import REPORT_PATH,DRIVER_PATH

CHROMEDRIVER_PATH = os.path.join(DRIVER_PATH,'chromedriver.exe')
IEDRIVER_PATH = os.path.join(DRIVER_PATH,'IEDriverServer.exe')
PHANTOMJSDRIVER_PATH = os.path.join(DRIVER_PATH,'phantomjs.exe')

TYPES = {'firefox':webdriver.Firefox,'chrome':webdriver.Chrome,'ie':webdriver.Ie,'phantomjs':webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox':'wires','chrome':CHROMEDRIVER_PATH,'ie':IEDRIVER_PATH,'phantomjs':PHANTOMJSDRIVER_PATH}

class UnSupportBrowserTypeError(Exception):
    pass

class Browser(object):
    def __init__(self,browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' %','.join(TYPES.keys()))
        self.driver = None

    def get(self,url,maximize_window=True,implicitly_wait=30):
        self.driver=self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.implicitly_wait(implicitly_wait)
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        return self

    def close(self):
        self.driver.close()
    def quit(self):
        self.driver.quit()

    def save_screen_shot(self,name='screen_shot'):
        day = time.strftime('%Y%m%d',time.localtime(time.time()))
        screen_path = REPORT_PATH + '\screenshot_%s' %day
        if not os.path.exists(screen_path):
            os.makedirs(screen_path)

        tm = time.strftime('%H%M%S',time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screen_path+'\\%s_%s.png' %(name,tm))
        return screenshot