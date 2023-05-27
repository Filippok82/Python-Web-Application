import time
import yaml
from BaseApp import BasePage
from testpage import Operations

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(er1, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login()
    page.enter_pass()
    page.click_login_button()
    assert page.get_error_text() == er1


def test_step2(er2, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_login02()
    page.enter_pass02()
    page.click_login_button02()
    time.sleep(2)
    assert page.get_error_hello() == er2


def test_step3(er3, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.new_post()
    page.enter_title()
    page.enter_description()
    page.enter_content()
    page.click_save_post()
    time.sleep(2)
    assert page.get_error_title() == er3


def test_step4(er4, browser):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.click_contact_us()
    page.enter_name()
    page.enter_email()
    page.enter_message()
    page.save_contact_us()
    time.sleep(2)
    assert page.check_alert() == er4
