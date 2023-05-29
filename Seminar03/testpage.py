import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging




class TestLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class Operations(BasePage, TestLocators):

    # ENTER TEXT
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} nit found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def enter_login(self, word):
        self.enter_text_into_field(TestLocators.ids["x_selector1"], word, description="Login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestLocators.ids["x_selector2"], word, description="Password form")

    def enter_title(self, word):
        self.enter_text_into_field(TestLocators.ids["title"], word, description="title")

    def enter_description(self, word):
        self.enter_text_into_field(TestLocators.ids["description"], word, description="description")

    def enter_content(self, word):
        self.enter_text_into_field(TestLocators.ids["content"], word, description="content")

    def enter_name(self, word):
        self.enter_text_into_field(TestLocators.ids["field_name"], word, description="name")

    def enter_email(self, word):
        self.enter_text_into_field(TestLocators.ids["field_email"], word, description="email")

    def enter_message(self, word):
        self.enter_text_into_field(TestLocators.ids["field_message"], word, description="message")

    # CLICK
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def click_login_button(self):
        self.click_button(TestLocators.ids["btn_selector"], description="login")

    def new_post(self):
        self.click_button(TestLocators.ids["btn_new_post"], description="new post")

    def click_save_post(self):
        self.click_button(TestLocators.ids["btn_save"], description="save post")

    def click_contact_us(self):
        self.click_button(TestLocators.ids["btn_contact_us"], description="contact us")

    def save_contact_us(self):
        self.click_button(TestLocators.ids["btn_save_contact_us"], description="save contact us")

    # GET TEXT
    def get_text_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def get_error_text(self):
        return self.get_text_element(TestLocators.ids["x_selector3"])

    def get_error_hello(self):
        return self.get_text_element(TestLocators.ids["x_selector4"])

    def get_error_title(self):
        return self.get_text_element(TestLocators.ids["check_title"])

    def check_alert(self):
        alert = self.driver.switch_to.alert
        text_alert = alert.text
        logging.info(f' {text_alert} ')
        return text_alert
