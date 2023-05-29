import logging
import time
import yaml
from BaseApp import BasePage
from testpage import Operations

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 Starting")
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login("test")
    page.enter_pass("test")
    page.click_login_button()
    time.sleep(2)
    assert page.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login(testdata["login"])
    page.enter_pass(testdata["passwd"])
    page.click_login_button()
    time.sleep(2)
    assert page.get_error_hello() == "Hello, {}".format(testdata["login"])


def test_step3(browser):
    logging.info("Test3 Starting")
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.new_post()
    page.enter_title(testdata["title"])
    page.enter_description(testdata["description"])
    page.enter_content(testdata["content"])
    page.click_save_post()
    time.sleep(2)
    assert page.get_error_title() == testdata["title"]


def test_step4(browser):
    logging.info("Test4 Starting")
    page = Operations(browser)
    page.click_contact_us()
    time.sleep(3)
    page.enter_name("Test sem3")
    page.enter_email("test_sem3@yandex.ru")
    page.enter_message("Message seminar3 homework3")
    time.sleep(2)
    page.save_contact_us()
    time.sleep(2)
    assert page.check_alert() == "Form successfully submitted"
