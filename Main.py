from pprint import pprint
from urllib.parse import urlencode
import os
import requests
from VK_API import VKAPIClient
from Yandex_API import YAAPIClient

if __name__ == '__main__':

    TOKEN_VK = os.environ['APIVK']
    user_id = 90991960
    vk_client = VKAPIClient(TOKEN_VK, user_id)
    list_photo = vk_client.get_photos()

    TOKEN_YA = os.environ['APIYA']
    client = YAAPIClient(TOKEN_YA)
    # print(client.list_dir('/'))
    # print(client.upload_file('Image', 'VK_API.py'))
    for nums, item in enumerate(list_photo):
        response = requests.get(item)
        if response.status_code == 200:
            with open('sample', 'wb') as f:
                f.write(response.content)
        with open('sample.jpg', 'rb') as file:
            client.upload_file('Image', file)


    # url = 'https://oauth.vk.com/authorize'
    # params = {
    #     'client_id': '51775885',
    #     'redirect_uri': 'https://oauth.vk.com/blank.html',
    #     'response_type': 'token',
    #     'scope': 'photos, status'
    # }
    # response = f'{url}?{urlencode(params)}'
    # print(response)
