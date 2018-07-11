# from selenium import webdriver
# import os
# import unittest
#
# class testcase(unittest.TestCase):
#     # os.system('taskkill /F /IM chrome.exe')
#     # os.system('taskkill /F /IM chromedriver.exe')
#
#     def setUp(self):
#
#         self.driver = webdriver.Chrome()
#         self.driver.get('http://127.0.0.1:5000')
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#     def tearDown(self):
#         pass
#
#     def test_case1(self):
#         self.driver.execute_script("document.getElementsByTagName('button')[1].style.visibility='visible'")
#
#         # JS = "document.getElementsByTagName('button')[1].style.visibility"
#         # print()
#
# if __name__=="__main__":
#     unittest.main(verbosity=2)

from selenium import webdriver
import os

os.system('taskkill /F /IM chrome.exe')
os.system('taskkill /F /IM chromedriver.exe')

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000')
driver.maximize_window()
driver.implicitly_wait(10)

driver.execute_script("document.getElementsByTagName('button')[1].style.visibility='visible'")
JS = "return document.getElementsByTagName('button')[1].style.visibility"
print(driver.execute_script(JS))