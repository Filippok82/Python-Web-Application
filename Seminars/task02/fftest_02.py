import requests

# def new_post():
#     p = requests.post('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
#     print(p.json())
#
# token= login()
#
# new_post()

p = requests.post('https://test-stand.gb.ru/api/posts', data={"username": 'alalalalal', "password": '3dfd64df7e'})
print(p.json())
