import requests
from urllib.parse import urlencode, urljoin
from pprint import pprint
"""Задача №1
Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.
Задача №2
Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих 
друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.
Задача №3
Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK
"""


TOKEN = '*******'
API_BASE_URL = "https://api.vk.com/method/"
V = '5.124'
ID = 0000000
class VKAPIClient:
    def __init__(self, token, version, id):
        self.token = token
        self.version = version
        self.id = id

    def finding_mutual_friends(self,id):
        friends_mutual_url = urljoin(API_BASE_URL, 'friends.getMutual')
        res = requests.get(friends_mutual_url, params={
            'source_uid': self.id,
            "target_uid": id,
            'access_token': self.token,
            "v": self.version

        })
        list_class = []
        for id in res.json()['response']:
            list_class.append(VKAPIClient(TOKEN, V, id))
        return list_class

    def __and__(self,other):
        return self.finding_mutual_friends(other.id)

    def __repr__(self):
        return f'VKAPIClient({TOKEN},{V},{self.id})'

    def output_link(self):
        return f'https://vk.com/id{self.id}'

my_account = VKAPIClient(TOKEN, V, ID)
other_account = VKAPIClient(TOKEN, V, 12345)

pprint(my_account & other_account)
# print(my_account.output_link())