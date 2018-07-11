from selenium.webdriver.common.by import By
from test.page.baidu_main_page import BaiDuMainPage

class BaiDuResultPage(BaiDuMainPage):
    locator_search_result = (By.XPATH,'//div[contains(@class,"result")]/h3/a')

    @property
    def result(self):
        return self.find_elements(*self.locator_search_result)