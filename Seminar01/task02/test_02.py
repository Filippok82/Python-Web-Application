"""Задание

Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».

Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/gateway/posts с передачей параметров title, description, content.
"""
import yaml
import requests

with open("logpass.yaml") as f:
    user = yaml.safe_load(f)


def new_post(token):
    response = requests.post("https://test-stand.gb.ru/api/posts", headers={'X-Auth-Token': token},
                             params={'title': user['title'],
                                     'description': user['description'],
                                     'content': user['content']})
    return response.json()


def my_post(token):
    response = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    listdesc = [i['description'] for i in response.json()['data']]
    return listdesc


def test_step3(login, checking_description):
    new_post(login)
    assert checking_description in my_post(login)
