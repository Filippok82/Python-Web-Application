import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope='session')
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)

    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def good():
    return "колбаса"


@pytest.fixture()
def bad():
    return "калбаса"


@pytest.fixture()
def login():
    r = requests.post('https://test-stand.gb.ru/gateway/login', data={'username': testdata["login"],
                                                                      'password': testdata["passwd"]})
    return r.json()['token']


@pytest.fixture()
def text1():
    return "Тест"

@pytest.fixture()
def checking_description():
    return 'A brief description of the new post'