import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can`t find element by locator {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, mode, locator, property):
        element = self.find_element(mode, locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.exception(f"Property {property} not fount in element with locator {locator}")
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Exception with alert")
            return None


    # class BasePage:
    # def __init__(self, driver):
    #     self.address = 'https://test-stand.gb.ru'
    #     self.driver = driver
    #
    # def start_browser(self):
    #     self.driver.get(self.address)
    #
    # def find_element(self, locator, time=10):
    #     return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
    #                                                   message=f'Cant find element by locator{locator}')
    #
    # def get_element_property(self, locator, property):
    #     element = self.find_element(locator)
    #     return element.value_of_css_property(property)

    # def go_to_site(self):
    #     return self.driver.get(self.address)
