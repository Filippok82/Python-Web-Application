"""Задание
Условие: Добавить в наш тестовый проект шаг добавления поста после входа.
Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста."""

import yaml
from Seminar02.module import Site
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, result):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")

    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")

    btn = site.find_element("css", btn_selector)
    btn.click()

    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == result


def test_step2(x_selector1, x_selector2, btn_selector, hello_user):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata['login'])

    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata['passwd'])

    btn = site.find_element("css", btn_selector)
    btn.click()

    time.sleep(3)
    element = site.find_element("xpath", hello_user)
    assert element.text == f"Hello, {testdata['login']}"


def test_step3(new_post, title, description, content, btn_save, check_title):
    time.sleep(1)
    btn1 = site.find_element("xpath", new_post)
    btn1.click()

    input1 = site.find_element("xpath", title)
    input1.send_keys(testdata['title'])

    input2 = site.find_element("xpath", description)
    input2.send_keys(testdata['description'])

    input3 = site.find_element("xpath", content)
    input3.send_keys(testdata['content'])
    time.sleep(1)
    btn2 = site.find_element("xpath", btn_save)
    btn2.click()
    time.sleep(2)
    element = site.find_element("xpath", check_title)
    assert element.text == testdata['title']

    site.close()
