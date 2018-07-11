from selenium.webdriver.common.by import By
from test.common.page import Page

class BaiDuMainPage(Page):
    locator_search_input = (By.ID,'kw')
    locator_search_button = (By.ID,'su')

    def search(self,kw):
        self.find_element(*self.locator_search_input).send_keys(kw)
        self.find_element(*self.locator_search_button).click()