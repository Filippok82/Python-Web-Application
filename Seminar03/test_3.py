import requests
import yaml

with open("testdata.yaml") as f:
    user = yaml.safe_load(f)


def get(token):
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token},
                     params={'owner': 'notMe'})
    listcont = [i['title'] for i in g.json()['data']]
    print(listcont)
    return listcont


def test_step2(login, text1):
    assert text1 in get(login)


def new_post(token):
    response = requests.post("https://test-stand.gb.ru/api/posts", headers={'X-Auth-Token': token},
                             data={'title': user['title'],
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
