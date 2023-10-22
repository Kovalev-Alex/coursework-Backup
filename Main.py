from pprint import pprint
import requests
import os
from VK_API import VKAPIClient
from Yandex_API import YAAPIClient

if __name__ == '__main__':

    TOKEN_VK = os.environ['APIVK']
    TOKEN_YA = os.environ['APIYA']
    # user_id = int(input('Введите ID пользователя (только цифры): '))
    user_id = 90991960
    vk_client = VKAPIClient(TOKEN_VK, user_id)
    pprint(vk_client.get_photos())

    client = YAAPIClient(TOKEN_YA)
    # print(client.list_dir('/'))
    print(client.upload_file('Image', 'VK_API.py'))
