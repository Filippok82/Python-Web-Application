import yaml

from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class TestLocators:
    x_selector1 = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    x_selector2 = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    x_selector3 = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    btn_selector = (By.CSS_SELECTOR, """button""")
    x_selector4 = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    btn_new_post = (By.XPATH, """//*[@id="create-btn"]""")
    title = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    description = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    content = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    btn_save = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    check_title = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    btn_contact_us = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    field_name = (By.XPATH, """//*[@id="contact"]/div[1]/label""")
    field_email = (By.XPATH, """//*[@id="contact"]/div[2]/label""")
    field_message = (By.XPATH, """//*[@id="contact"]/div[3]/label""")
    btn_save_contact_us = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class Operations(BasePage, TestLocators):

    def enter_login(self):
        logging.info('Enter login ')
        input1 = self.find_element(self.x_selector1)
        input1.send_keys("test")

    def enter_pass(self):
        logging.info('Enter password ')
        input2 = self.find_element(self.x_selector2)
        input2.send_keys("test")

    def click_login_button(self):
        logging.info('Click button ')
        btn = self.find_element(self.btn_selector)
        btn.click()

    def get_error_text(self):
        err_label = self.find_element(self.x_selector3)
        text = err_label.text
        logging.info(f'Error {text} ')
        return text

    def enter_login02(self):
        logging.info('Enter valid login ')
        input1 = self.find_element(self.x_selector1)
        input1.send_keys(testdata["login"])

    def enter_pass02(self):
        logging.info('Enter password ')
        input2 = self.find_element(self.x_selector2)
        input2.send_keys(testdata["passwd"])

    def click_login_button02(self):
        logging.info('Click button ')
        btn = self.find_element(self.btn_selector)
        btn.click()

    def get_error_hello(self):
        err_label = self.find_element(self.x_selector4)
        text = err_label.text
        logging.info(f'Error {text} ')
        return text

    def new_post(self):
        btn = self.find_element(self.btn_new_post)
        btn.click()

    def enter_title(self):
        logging.info('Enter title new post')
        input1 = self.find_element(self.title)
        input1.send_keys(testdata["title"])

    def enter_description(self):
        logging.info('Enter description new post')
        input2 = self.find_element(self.description)
        input2.send_keys(testdata["description"])

    def enter_content(self):
        logging.info('Enter content new post')
        input3 = self.find_element(self.content)
        input3.send_keys(testdata["content"])

    def click_save_post(self):
        logging.info('Click button save new post')
        btn = self.find_element(self.btn_save)
        btn.click()

    def get_error_title(self):
        err_label = self.find_element(self.check_title)
        text = err_label.text
        logging.info(f'Error {text} ')
        return text

    def click_contact_us(self):
        btn = self.find_element(self.btn_contact_us)
        btn.click()

    def enter_name(self):
        logging.info('Enter name ')
        input1 = self.find_element(self.field_name)
        input1.send_keys(testdata["name"])

    def enter_email(self):
        logging.info('Enter email')
        input1 = self.find_element(self.field_email)
        input1.send_keys(testdata["email"])

    def enter_message(self):
        logging.info('Enter message')
        input1 = self.find_element(self.field_message)
        input1.send_keys(testdata["message"])

    def save_contact_us(self):
        btn = self.find_element(self.btn_save_contact_us)
        btn.click()

    def check_alert(self):
        alert = self.driver.switch_to.alert
        text_alert = alert.text
        logging.info(f'Error {text_alert} ')
        return text_alert
