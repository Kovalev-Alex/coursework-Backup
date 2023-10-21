from pprint import pprint
import requests
import os
from VK_API import VKAPIClient


TOKEN = os.environ['APIVK']
user_id = int(input('Введите ID пользователя (только цифры): '))

vk_client = VKAPIClient(TOKEN, user_id)
pprint(vk_client.users_info())
